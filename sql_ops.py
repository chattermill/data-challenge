import sqlite3 as sql
import pandas as pd


# specify source file
f = 'reviews_cleaned.csv'

def fix_column_name(df):
	df.rename(columns = {'app_bought':'apps_bought'}, inplace = True)
	return df

def insert_data(df,conn):
	# map column name
	df = fix_column_name(df)
	# insert rows
	df.to_sql('reviews',conn, if_exists = 'append',index=False)
	print('INSERT SUCCESS')

def main():
	# connect to db
	conn = sql.connect('exercise_database.db')
	c = conn.cursor()
	df = pd.read_csv(f,index_col=False)
	insert_data(df,conn)

	# queries
	print('AVERAGE SCORE BY ISO')
	c.execute('SELECT iso,AVG(score) FROM reviews GROUP BY iso')
	for row in c.fetchall()[:5]:
		print(row[0],row[1])
	print('\n')

	print('MAXIMUM SCORE PER APPS BOUGHT BUCKET')
	c.execute('SELECT apps_bought_bucket,MAX(score) FROM reviews GROUP BY apps_bought_bucket')
	for row in c.fetchall()[:5]:
		print(row[0],row[1])
	print('\n')

	print('AVERAGE SCORE BY DATE')
	avg_score_date = c.execute('SELECT date,AVG(score) FROM reviews GROUP BY date ORDER BY date DESC')
	for row in c.fetchall()[:5]:
		print(row[0],row[1])
	print('\n')

main()