import sqlite3
import pandas as pd

def populate_database(database_path, data_path):

    try:
        data = pd.read_csv(data_path)
        
        database = sqlite3.connect(database_path)
        cursor = database.cursor()
        
        """This could be made modular like the sql queries but as it is just
        one command for now, this seems an acceptable solution"""
        sql_insert_reddit_database = '''INSERT INTO reviews(review, title, iso,
                                        score, date, apps_bought, money_spent, 
                                        apps_bought_bucket, money_spent_bucket)
                                        VALUES(?,?,?,?,?,?,?,?,?)'''
        
        """This turns every row into a tuple which is used by executemany"""
        tupled_data = [tuple(i) for i in data.values]
        
        """Executes the command and the data to use"""
        cursor.executemany(sql_insert_reddit_database,tupled_data)
        database.commit()
        database.close()
    except Exception as e:
        print(e)


populate_database("exercise_database.db", "reddit_exercise_data_clean.csv")

"""NB I did see that there was a one-line code you coud use to add a pandas
dataframe to SQL but 1) I've never used SQL before so it was more fun to learn
it and 2) it felt like it was going against the "spirit" of the challenge"""