import pandas as pd
import re
from datetime import datetime

def strip_dates(date):
    #removes anything after the space
    return re.sub(r' .*$', '', date)

def uniform_format_dates(date):
    """Changes the format of the years in the "data" column to be uniform.
    Assumes that this data is the limit of the odd date formats."""
    if "/" in date:
        return datetime.strptime(date, '%m/%d/%y').strftime('%Y-%m-%d')
    else:
        try:
            return datetime.strptime(date, '%y-%m-%d').strftime('%Y-%m-%d')
        except:
            return date

def clean_dates(date):
    date = strip_dates(date)
    date = uniform_format_dates(date)
    return date

def clean_data(dirty_data_location):
    data = pd.read_csv(dirty_data_location, index_col=0)
    
    """quantile bucketing because otherwise we could get meaningless buckets if
    we get outliers. I chose 5 buckets arbitrarily"""
    data['app_bought_bucket'] = pd.qcut(data['app_bought'], 5)
    data['money_spent_bucket'] = pd.qcut(data['money_spent'], 5)
    
    """Inspection of data shows that date formats are inconsistent"""
    data['date'] = data['date'].apply(clean_dates)      
    
    """product_name contains no unique info, delete"""
    data = data.drop(columns="product_name")
    
    """Creates a new .csv file for us"""
    data.to_csv('reddit_exercise_data_clean.csv')
    
    return None
    

dirty_data_location = 'reddit_exercise_data.csv'
clean_data(dirty_data_location)










