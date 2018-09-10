import sqlite3
import pandas as pd
import csv


class dbHandler:
    
    
    def __init__(self, path=None):
        self.conn = None
        self.cur = None
        if path:
            self.retrieve(path)
            
    def retrieve(self,path):
        self.conn = sqlite3.connect(path);
        self.cursor = self.conn.cursor()

    def terminate(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def init_db_table(self, table, query):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS "+ table)
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as error:
            print('Couldnt initiate table '+ table + "\nError: " + str(error))
            self.conn.rollback()
            raise SystemExit('Error while initiating')
            
    """
    Populate an existing table using a csv file and columns to add.
    """
    def populate_table_csv(self, file, table, columns):
        with open(file,'r',encoding='utf8') as reviews_table:
            d_reviews = csv.DictReader(reviews_table)
            to_db = [[i[col] for col in columns] for i in d_reviews]
        try:
            self.cursor.executemany("INSERT INTO " +table+ " VALUES ("+ "?"+ ",?"*(len(columns)-1)+");", to_db) #Allows to populate tables with varying column numbers
            self.cursor.close()
            self.conn.commit()
        except sqlite3.Error as error:
            print('Couldnt populate table '+ table + "\nError: " + str(error))
            self.conn.rollback()
            raise SystemExit('Error while populating')
            
    def query_to_df(self, query):
        df = pd.read_sql_query(query, self.conn) 
        return df
    
def main():
    db = dbHandler(path="exercise_database.db")
    table = 'reviews'
    query = "CREATE TABLE " + table + """ (title TEXT,
                                          review TEXT,
                                          iso TEXT,
                                          score INTEGER,
                                          date TEXT,
                                          apps_bought INTEGER,
                                          money_spent INTEGER,
                                          apps_bought_bucket INTEGER,
                                          money_spent_bucket INTEGER)"""
    db.init_db_table(table, query)
    columns = ['title', 'review', 'iso', 'score', 'date','apps_bought', 'money_spent', 'apps_bought_bucket','money_spent_bucket']
    table = 'reviews'
    path = 'reddit_exercise_data_cleaned.csv'
    db.populate_table_csv(path,table, columns)
    get_avg_score_iso = """SELECT iso,
                                  AVG(score) as Average_score
                                  FROM reviews 
                                  GROUP BY iso 
                                  ORDER BY iso;"""
    
    get_max_score_apps_bought = """SELECT apps_bought_bucket,
                                          MAX(score) as Max_score
                                          FROM reviews 
                                          GROUP BY apps_bought_bucket 
                                          ORDER BY apps_bought_bucket;"""
    
    get_avg_score_overtime ="""SELECT date,
                                      AVG(score) as Average_score
                                      FROM reviews 
                                      GROUP BY date
                                      ORDER BY date;"""
    q1 = db.query_to_df(get_avg_score_iso)
    q2 = db.query_to_df(get_max_score_apps_bought)
    q3 = db.query_to_df(get_avg_score_overtime)
    q1.to_csv('Average score by iso.csv', index=False)
    q2.to_csv('Maximum score by app_bought_bucket.csv', index=False)
    q3.to_csv('Average score over time (day).csv', index=False)
    print("Average Score by ISO:\n " ,q1.head(),"\n\n\n ")
    print("Max Score by apps bought:\n " ,q2.head(),"\n\n\n ")
    print("Average Score by date: \n" ,q3.head())
    db.terminate()

if __name__ == "__main__":
    main()
