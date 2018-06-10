'''import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from sklearn.feature_extraction.text import TfidfVectorizer

email_corpus = ['mail my policy','send me my cards','email my policy id card']

td_vector = TfidfVectorizer(sublinear_tf=True, stop_words='english')

result_vector = td_vector.fit_transform(email_corpus)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
tr = count_vect.fit_transform(email_corpus)

print(tr)
print(result_vector)
print("***************")
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(tr)

print(X_train_tfidf)
import pickle
from sklearn.feature_extraction.text import CountVectorizer

filename = 'model_loc/multiNB_countvec.pkl'
cv=pickle.load(open(filename, 'rb'))

s=pickle.load(open('model_loc/multiNB.pkl','rb'))

phrase = ['send my car auto policy document?']

y_data = cv.transform(phrase)

print(y_data)

print(s.predict(y_data))'''

import pickle
from sklearn.feature_extraction.text import CountVectorizer

phrase = 'send my car auto policy document?'

count_vec = CountVectorizer(stop_words='english')
vec = count_vec.build_tokenizer()

print(count_vec.build_tokenizer()(phrase))
