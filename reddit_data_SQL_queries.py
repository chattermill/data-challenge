import sqlite3
import pandas as pd

commands = {
"avg_score_by_iso_grouping": '''SELECT iso, AVG(score) 
                                FROM reviews 
                                GROUP BY iso''',
"max_score_by_app_bought_grouping": '''SELECT apps_bought_bucket, MAX(score)
                                        FROM reviews
                                        GROUP BY apps_bought_bucket''',
"avg_score_over_time_grouping": '''SELECT date, AVG(score)
                                    FROM reviews
                                    GROUP BY date'''
                                    }

def sql_query(command, database_path):
    try:
        database = sqlite3.connect(database_path)
        cursor = database.cursor()
        cursor.execute(command)
        queried_data = cursor.fetchall()
        
        database.close()
        return queried_data
    
    except Exception as e:
        print(e)

def write_all_to_csv(database_path):
    for key, value in commands.items():
        query_result = sql_query(value, database_path)
        dataframe = pd.DataFrame(query_result)
        dataframe.to_csv(key + ".csv")
        
        
write_all_to_csv("exercise_database.db")










