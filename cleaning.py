import pandas as pd


# specify source file
file = "reddit_exercise_data.csv"

def generate_buckets(data):
	data['apps_bought_bucket'] = pd.cut(data.app_bought, [0,20,40,60,500],labels = ['<20','20-40','40-60','>60'])
	data['money_spent_bucket'] = pd.qcut(data.money_spent,5,labels=["1st_quantile","2nd_quantile","3rd_quantile","4th_quantile","5th_quantile"])
	data['apps_bought_bucket'] = data.apps_bought_bucket.astype(str)
	data['money_spent_bucket'] = data.money_spent_bucket.astype(str)
	return data

def clean_date(data):
	dates = data.date.values.tolist()
	dates_clean = [pd.to_datetime(date) for date in dates]
	data['date'] = dates_clean
	# remove the time in datetime since every row has same value 0:0:0
	data['date'] = data.date.dt.date
	return data

def drop_column(data,cols):
	data.drop(cols,axis=1,inplace=True)
	return data

def main():
	df = pd.read_csv(file,index_col=False)
	df = clean_date(df)
	df = generate_buckets(df)
	df = drop_column(df,['title','product_name'])
	print(df.head())
	df.to_csv('reviews_cleaned.csv',index=False)

if __name__ == "__main__":
	main()
