class random_predict(object):

    def __init__(self, Xtest_data):
        self.predict(Xtest_data)

    def predict(self, xtest_ph):
        import pickle
        from sklearn.feature_extraction.text import CountVectorizer

        filename = 'model_loc/randomf_countvec.pkl'
        cv=pickle.load(open(filename, 'rb'))
        
        y_data = cv.transform([xtest_ph])
        s=pickle.load(open('model_loc/randomf.pkl','rb'))

        result = s.predict(y_data)

        sprob = s.predict_proba(y_data)
        
        print(result)

        print(sprob)
