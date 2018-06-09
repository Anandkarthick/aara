import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model

email_df = pd.read_csv('train/test.csv')
email_corpus = email_df['content']
td_vector = TfidfVectorizer(stop_words='english')
result_vector = td_vector.fit_transform(email_corpus)

print(type(email_corpus))
