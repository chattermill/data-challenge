# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3

queries_dict = {
    'average_score_by_iso': """SELECT iso ,AVG(score) FROM reviews GROUP BY iso """,
    'max_score_by_app_bucket': """SELECT app_bought_bucket , MAX(score) FROM reviews GROUP BY app_bought_bucket """,
    'average_score_over_time': """SELECT  date , AVG(score) FROM reviews GROUP BY date ORDER BY date(date)"""
}
#generate one CSV per query:
def run_queries(db_path):
    connection = sqlite3.connect(db_path)
    
    for key , value in queries_dict.items():
        new_df = pd.read_sql(value, con=connection)
        new_df.to_csv(f'results/{key}.csv' ,  index=False)

    connection.close()