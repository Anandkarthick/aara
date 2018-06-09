'''
import content_eval as cte

result = cte.content_eval('email')
print(result)


import pandas as pd

email_df = pd.read_csv('train/email.csv')

email_corpus = email_df['content']

from sklearn.feature_extraction.text import TfidfVectorizer

td_vector = TfidfVectorizer(stop_words='english')

result_vector = td_vector.fit_transform(email_corpus)

print(result_vector.mean())

import feature_train as ft

act_ft = ft.feature_train('email_auto')
print(act_ft.selection())

from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer

email_corpus = ['mail my policy','send me my cards','email my policy id card']

td_vector = TfidfVectorizer(sublinear_tf=True, stop_words='english')

result_vector = td_vector.fit_transform(email_corpus)

X_train = result_vector
Y_train = ['policy','card','pol']
clf = linear_model.SGDClassifier()
clf.fit(X_train,Y_train)

'''
