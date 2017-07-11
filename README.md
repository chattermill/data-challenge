# data-challenge
A short technical challenge for data analyst candidates

### Goal
We would like you to demonstrate your skills in simple data manipulation and analysis. We are looking to understand how you approach the problem and knowledge of python/SQL and/or ability to learn new things on the fly.

### Data
We have provided you with a dataset of app reviews for the popular reddit app. The csv file has multiple flaws and falls short of what we would like to work with, as is often the case and therefore want you to fix it.

### Expected Output
We expect you to parse the file and make sure that things are consistent and as orderly as possible. For example the app_bought and money_spent variables should be available in desirable buckets. We will leave it to you to define what is desirable. 

You should produce three outputs:
1. A new csv file with all the data in a format that is desirable to input into any system
2. We would want you to populate the  **reviews** table in exercise_database.db. It holds the following columns:

review | title | iso | score | date | apps_bought | money_spent | apps_bought_bucket | money_spent_bucket
--- | --- | --- | --- |--- |--- |--- |--- |--- 
TEXT | TEXG | TEXT | INTEGER | TEXT | INTEGER | NUMERIC | TEXT | TEXT 

3. You should write SQL queries to fetch the following metrics from the **reviews** table. 
	1. Average per iso
	2. Average score per app_bought_bucket
	3. Average score overtime (weekly)
The outputs should be available in an excel/google sheet file with graphs

### Notes

- You should be able to complete the project within a few hours, not days.
- Feel free to work in whatever language / framework you are most comfortable in, but we prefer Python for datascience tasks.
- Please focus on making the code clear and modular, rather than on the complexity of the solution. Treat your code as if it will be deployed to production. Which would mean taking into account things changing in the incoming data format, such as columns moving. 




