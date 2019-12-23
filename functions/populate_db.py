# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3

def populate_db(db_path, clean_data_path):
    connection = sqlite3.connect(db_path)
    clean_data = pd.read_csv(clean_data_path)
    clean_data.to_sql(name = 'reviews', con = connection, if_exists = 'replace', index = False)
    connection.close()