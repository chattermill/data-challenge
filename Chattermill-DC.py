import emoji
import sqlite3
import pandas as pd
import numpy as np
df = pd.read_csv('./reddit_exercise_data.csv', sep=',', escapechar='\n')
df.rename({'app_bought': 'apps_bought'}, axis=1,  inplace=True)
df.drop(['product_name'], axis=1, inplace=True)


def parse_dates(df):
    """There are 3 distinct date formats as per length of the string
    the last will need to be parsed separately since day is occuring first
    There must be more efficient way of doing it with pd.datetime.strptime()
    but this does it for now"""
    
    idx_1 = df.date[df.date.str.len() < 11].index
    idx_2 = df.date[df.date.str.len() > 11].index
    
    for i in idx_1:
        df.loc[i, 'date'] = pd.to_datetime(df.date[i], dayfirst=True, infer_datetime_format=True)
    for i in idx_2:
        df.loc[i, 'date'] = pd.to_datetime(df.date[i], yearfirst=True, infer_datetime_format=True)
    df['date'] = pd.to_datetime(df.date)
    return df


def make_buck(df):
    """Create equaly spaced buckets, alternatively use
    pd.qcut() to create balanced bukets"""
        
    lbl_app = ['0-20', '20-40', '40-60', '60-80', '80-100']
    df['apps_bought_bucket'] = pd.cut(df.apps_bought, bins = 5, labels=lbl_app)
    lbl_mon = ['0-100', '100-200', '200-300', '300-400', '400-500']
    df['money_spent_bucket'] = pd.cut(df.money_spent, bins = 5, labels=lbl_mon)
    return df


def preprocessing(df):
    """Create lists of features based on dtype, for indexing and cleaning
    we could also remove non word"""
    cp = df[:]
    parse_dates(cp)
    make_buck(cp)
    num_feat = []
    cat_feat = []
    dt = []
    for i in cp:
        if cp[i].dtype == np.int64 or cp[i].dtype == np.float64:
            num_feat.append(i)
        elif cp[i].dtype == 'datetime64[ns]':
            dt.append(i)
        else:
            cat_feat.append(i)
    for i in cat_feat[:3]:
        #Remove carriage return
        cp[i] = cp[i].str.replace(r'\r', '')
        cp[i] = cp[i].str.replace(r'r/', '')
        cp[i] = cp[i].str.lower()
        #df[i] = df[i].str.replace('[^\w\s]', '')
    #'category' type seems to require less memory for the below columns
    cp['iso'] = cp['iso'].astype('category')
    return cp


x = preprocessing(df)
x.to_csv('DL_preprocessed.csv')


def pop_reviews(df, db_file):
    """populate the db file and close connection"""
    
    db = sqlite3.connect(db_file)
    c = db.cursor()
    c.execute('DELETE FROM reviews')
    df.to_sql('reviews', db, if_exists='append', index=False)
    c.close()
    return None


pop_reviews(x, './exercise_database.db')


def avg_score_iso(db_file):
    """create a csv with the avg score by iso"""
    
    db = sqlite3.connect(db_file)
    f_1 = pd.read_sql('SELECT iso, AVG(score) as avg_by_iso FROM reviews GROUP BY iso ORDER BY avg_by_iso ASC', db)
    f_1.to_csv('./avg_by_iso.csv')
    db.close()
    return f_1[:3]


avg_score_iso('./exercise_database.db')


def maximum_score_by_apps_bought_bucket(db_file):
    """create a csv with the max score by apps_bought_bucket"""
    
    db = sqlite3.connect(db_file)
    f_2 = pd.read_sql('SELECT apps_bought_bucket, MAX(score) as Max_score FROM reviews GROUP BY apps_bought_bucket ORDER BY Max_score ASC', db)
    f_2.to_csv('./Max_score_by_app_bucket.csv')
    db.close()
    return f_2


maximum_score_by_apps_bought_bucket('./exercise_database.db')


def avg_score_day(db_file):
    """create a csv with the avg score by day"""
    
    db = sqlite3.connect(db_file)
    f_3 = pd.read_sql('SELECT date, AVG(score) as avg_day FROM reviews GROUP BY date ORDER BY avg_day ASC', db)
    f_3.to_csv('./avg_day.csv')
    db.close()
    return f_3[:3]


avg_score_day('./exercise_database.db')


def avg_score_day_week(db_file):
    """create a csv with the avg score by day of week
    Sunday == 0 etc"""
    
    db = sqlite3.connect(db_file)
    f_4 = pd.read_sql('SELECT strftime("%w", date) as day, AVG(score) as avg_by_day_week FROM reviews GROUP BY day ORDER BY avg_by_day_week ASC', db)
    f_4.to_csv('./avg_day_week.csv')
    db.close()
    return f_4

avg_score_day_week('./exercise_database.db')