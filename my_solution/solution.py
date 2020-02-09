#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:40:27 2020

@author: Yukti Garg
This script reads the input csv file and writes cleaned output to another csv and database
To use this script: 
    python solution.py <input_csv_file> <output_csv_file> <desired_db_name> <desired_table_name>
    Example Usage:
       python solution.py ../reddit_exercise_data.csv reviews.csv exercise_database.db reviews
"""

import pandas as pd
import sqlite3
import datetime
import sys

def format_date(input_date):
    idate = input_date.split(" ")[0]
    if idate.find('/') >= 0:
        month,date,year = [int(x) for x in idate.split('/')]
    else:
        year,month,date = [int(x) for x in idate.split('-')]
    year = 2000+year if year < 2000 else year
    return datetime.date(year,month,date).strftime("%d-%m-%Y")

def bucket_string(base, number):
    return str(number//base*base)+"-"+str((number//base+1)*base)
    
def augment_with_buckets(reviews_df):
    reviews_df['app_bought_bucket'] = reviews_df.app_bought.apply(lambda x: bucket_string(10,x))
    reviews_df['money_spent_bucket'] = reviews_df.money_spent.apply(lambda x: bucket_string(25,x))
    return reviews_df

def clean_dataframe(df):
    df.drop_duplicates(keep=False,inplace=True)
    df.date = df.date.apply(format_date)
    return df

def write_to_database(df, db_name, tbl_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(tbl_name, conn, index=False, if_exists='replace')
    conn.close()
    return
    
def prepare_csv_database(df, csv_filename, db_name, tbl_name):
    df = clean_dataframe(df)
    df.to_csv(csv_filename)
    df = augment_with_buckets(df)
    df = df[['review','title','iso','score','date','app_bought','money_spent','app_bought_bucket','money_spent_bucket']]
    write_to_database(df, db_name, tbl_name)
    return

if __name__ == "__main__":
    script, input_file, output_file, db_name, table_name = sys.argv
    reviews_df = pd.read_csv(input_file)
    prepare_csv_database(reviews_df, output_file, db_name, table_name)