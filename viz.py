import pandas as pd
import matplotlib.pyplot as plt

# specify source file
file = "reddit_exercise_data.csv"
df = pd.read_csv(file,index_col=False)
print(df.head())
print(df.describe())

apps_bought = df.app_bought.unique().tolist()
num_count = df.app_bought.value_counts()

plt.bar(apps_bought,num_count)
plt.show()