# -*- coding: utf-8 -*-
import pandas as pd
import datetime

def clean_data(csv_path):
    #    read the csv file
    df = pd.read_csv(csv_path , encoding='utf-8',)
    
    #    make money_spent a float to be converted to NUMERIC data type in SQLite
    df['money_spent'] = df['money_spent'].apply(lambda x: float(x))
    
    #    product_name only has one value (used df['product_name'].value_counts() to see that) telling us this is about the Reddit app.
    # Therefore it brings no information so we delete it
    del df['product_name']
    
    # Every row's time is 00:00 so the time information is useless that date column is a datetime.
    # Also, the date format changes between rows
    # So let's make this column a date string in a format that SQLite will interpret as date https://www.sqlite.org/lang_datefunc.html
    #  all dates have year first, except for the ones uysing / instead of -
    # transforming the  dates to a "year first" date format.
    def change_to_year_first_format(date_string):
        if '/' in date_string:
            return datetime.datetime.strptime(date_string, '%m/%d/%y').strftime('%Y-%m-%d')
        else:
          return date_string

    df['date'] = df['date'].apply(change_to_year_first_format)
    df['date'] = pd.to_datetime(df['date'], yearfirst=True).apply(lambda x: x.strftime('%Y-%m-%d'))
    
#    Create columns with bins for apps_bought and money_spent.
    
    # Given the EDA, I could have used the following bins:
    # bins_apps = [-1, 1, 5, 10, 25, 50, 100]
    # bins_money = [-1, 1, 5, 10, 50, 100,200,300,400,450,500]
    # but not sure of the business requirements, and given that this needs to be production ready for any data,
    # I prefer using X bins of the same size. 
    df['app_bought_bucket'] = pd.cut(df['app_bought'], 20)    
    df['money_spent_bucket'] = pd.cut(df['money_spent'], 20)
    
    return df
