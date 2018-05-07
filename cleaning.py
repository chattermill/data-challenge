import pandas as pd


# specify source file
file = "reddit_exercise_data.csv"

def generate_buckets(data):
	data['apps_bought_bucket'] = pd.cut(data.app_bought, [0,20,40,60,500],labels = ['<20','20-40','40-60','>60']).astype(str)
	data['money_spent_bucket'] = pd.qcut(data.money_spent,4,labels=['1st quartile','2nd quartile','3rd quartile','4th quartile']).astype(str)
	return data

def main():
	df = pd.read_csv(file,index_col=False)
	df = generate_buckets(df)
	print(df.head())
	df.to_csv('data_with_bucket.csv',index=False)

if __name__ == "__main__":
	main()
