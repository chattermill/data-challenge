import pandas as pd
import matplotlib.pyplot as plt

# specify source file
file = "reddit_exercise_data.csv"
df = pd.read_csv(file,index_col=False)
print(df.head())
print(df.describe())


apps_bought = df.app_bought.unique().tolist()
num_count = df.app_bought.value_counts()
plt.subplot(2,1,1)
plt.title('Apps Bought')
plt.bar(apps_bought,num_count)

money_spent = df.money_spent.unique().tolist()
spending_count = df.money_spent.value_counts()
plt.subplot(2,1,2)
plt.title('Money Spent')
plt.bar(money_spent,spending_count)

plt.show()