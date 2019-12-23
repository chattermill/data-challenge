# -*- coding: utf-8 -*-
from functions.data_cleaning import clean_data
from functions.populate_db import populate_db
from functions.sql_queries import run_queries


#Give the path of the CSV file:
original_csv_path = 'reddit_exercise_data.csv'
#Call the data_cleaning function that creates the clean Dataframe:
df = clean_data(original_csv_path)
#create a variable with the path of the clean data
clean_data_path = 'results/clean_data.csv'
#save clean data to CSV file:
df.to_csv(clean_data_path, encoding='utf-8', index=False)

db_path = 'exercise_database.db'
#Call the function to populate the database:
populate_db(db_path, clean_data_path)

#Run metrics SQL queries and save results to separate CSV files:
run_queries(db_path)
