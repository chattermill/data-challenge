# data-challenge
A short technical challenge for data analyst candidates
### Goal
We would like you to demonstrate your skills in simple data manipulation and analysis. We are looking to understand how you approach the problem and knowledge and/or ability to learn new things on the fly.

### Data
We have provided you with a dataset of app reviews for the popular reddit app. The csv file has multiple flaws and falls short of what we would like to work with, as is often the case.

### Expected Output
We expect you to parse the file and make sure that things are consistent and as orderly as possible. For example the app_bought and money_spent variables should be available in desirable buckets. We will leave it to you to define what is desirable. 

You should produce two outputs:
1. A new csv file with all the data in a format that is desirable to input into any system
2. We would want you to populate the exercise_database.db database file. There are two tables: 
  i. reviews, which should be constructed as the csv file. It holds the following columns:
  	review | title | iso | score | date | apps_bought | money_spent | apps_bought_bucket | money_spent_bucket
	--- | --- | --- | --- |--- |--- |--- |--- |--- 
	TEXT | TEXG | TEXT | INTEGER | TEXT | INTEGER | NUMERIC | TEXT | TEXT 



  ii. bought_coeffiecients, which should have the results of the regression score ~ money_spent as in the example table below