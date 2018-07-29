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
TRAIN_DATA = [('send my car id card',{ 'entities': [(12, 19, 'IDENTITY DOCUMENT')]})
('send my car insurance identity card', { 'entities': [(12, 35, 'IDENTITY DOCUMENT') , (12, 21, 'INSURANCE')]})
('send my auto id card', { 'entities': [(13, 20, 'IDENTITY DOCUMENT')]})
('send my auto identity card', { 'entities': [(13, 26, 'IDENTITY DOCUMENT')]})
('send my auto insurance card', { 'entities': [(13, 27, 'IDENTITY DOCUMENT') , (13, 22, 'INSURANCE')]})
('send auto insurance card', { 'entities': [(10, 24, 'IDENTITY DOCUMENT') , (10, 19, 'INSURANCE')]})
('mail my auto insurance identity card', { 'entities': [(13, 36, 'IDENTITY DOCUMENT') , (13, 22, 'INSURANCE')]})
('mail my auto insurance card', { 'entities': [(13, 27, 'IDENTITY DOCUMENT') , (13, 22, 'INSURANCE')]})
('mail my car insurance id card', { 'entities': [(12, 29, 'IDENTITY DOCUMENT') , (12, 21, 'INSURANCE')]})
('send my home id card', { 'entities': [(13, 20, 'IDENTITY DOCUMENT')]})
('send my home identity card	', { 'entities': [(13, 26, 'IDENTITY DOCUMENT')]})
('send my home insurance card', { 'entities': [(13, 27, 'IDENTITY DOCUMENT') , (13, 22, 'INSURANCE')]})
('send my insurance card', { 'entities':	[(8, 22, 'IDENTITY DOCUMENT') , (8, 17, 'INSURANCE')]})]