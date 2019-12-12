# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:42:17 2019

@author: loren
"""
import pandas as pd
import csv
import pymysql

df=pd.read_csv('Final1.csv',quoting=csv.QUOTE_ALL)
df.head()
conn=pymysql.connect(database='Exercise_database',user='root',password='nouazecisiunu_91')
cursor=conn.cursor()
cursor.execute('SELECT*FROM reviews;')
insert_query='INSERT INTO reviews VALUES'
print(insert_query)

for i in range(df.shape[0]):
    insert_query+= '('
    for j in range(df.shape[1]):
        insert_query += str(df[df.columns.values[j]][i])+ ','
    insert_query=insert_query[:-2] + '),'
insert_query = insert_query[:-1] + ';'
insert_query
cursor.execute(insert_query)
conn.commit()
