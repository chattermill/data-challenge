# data-challenge
A short technical challenge for data analyst candidates
### Goal
We would like you to demonstrate your skills in simple data manipulation and analysis. We are looking to understand how you approach the problem and knowledge and ability to learn new things on the fly.

### Data
We have provided you with a dataset app reviews for the popular reddit app. The csv file has multiple flaws and falls short of what we would like to work with, as is often the case.

### Expected Output
We expect you to parse the file and make sure that things are as orderly as possible. For example the app_bought and money_spent variables should be put in desirable buckets. We will leave it to you to define what is desirable. 

You should produce two outputs:
1. A new csv file with all the data in format that is desirable to input into any system
2. We would want you to populate the reddit_exercise_data.csv database file. There are two tables: 
  reviews, which should be constructed as the csv file.
  bought_coeffiecients, which should have the results of the regression score ~ money_spent as in the example table below