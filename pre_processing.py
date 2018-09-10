import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


"""
Clean series
Using stemming=True makes the function on average 40 times slower on this dataset. 
"""
def cleanText(series, stemming=False):
    banned_words = set(stopwords.words("english")) #Fetch common stopwords using nltk, convert to set to get O(1) lookup
    series = series.replace('[^\w\s]', '',regex=True) #Allows non EN chars but not punct / emojis etc
    if stemming: #Very slow
        ps = PorterStemmer()
        series = series.apply(lambda x: " ".join([ps.stem(item) for item in x.lower().split(' ') if item not in banned_words]))
    else:
        series = series.apply(lambda x: " ".join([item for item in x.lower().split(' ') if item not in banned_words]))
    return series

"""
Bin series by quantiles. 
Using labels=True will return the quantile number other than the interval
"""
def groupNumbers(series, q=4, set_labels=False):
    labels = [i for i in range(1,q+1)]
    series = pd.qcut(series,q, labels=(labels if set_labels else None))
    return series

if __name__ == "__main__":
    dataset_path = "C:/Users/JeanMalo.Delignon/Downloads/2013_ALL/reddit_exercise_data.csv"
    df = pd.read_csv(dataset_path,parse_dates=['date'])
    df.rename(columns = {'app_bought':'apps_bought'}, inplace = True)
    df['title'] = cleanText(df['title'], stemming=True)
    df['review'] = cleanText(df['review'], stemming=False)
    df['apps_bought_bucket'] = groupNumbers(df['apps_bought'],5,set_labels=True)
    df['money_spent_bucket'] = groupNumbers(df['money_spent'],5,set_labels=True)
    df.to_csv('reddit_exercise_data_cleaned.csv', index=False)    
