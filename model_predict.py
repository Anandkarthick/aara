class model_predict(object):

    def return_intent(self):
        return self.intent
    
    def __init__(self, Xtest_data):
        self.intent = " "
        self.predict(Xtest_data)

    def predict(self, xtest_ph):
        import pickle
        from sklearn.feature_extraction.text import CountVectorizer

        filename = 'model_loc/multiNB_countvec.pkl'
        cv=pickle.load(open(filename, 'rb'))
        print(xtest_ph)
        y_data = cv.transform([xtest_ph])
        s=pickle.load(open('model_loc/multiNB.pkl','rb'))

        result = s.predict(y_data)

        sprob = s.predict_proba(y_data)
        
        print(s.predict_log_proba(y_data))
        
        self.intent = result
        print(result)

        print(sprob)
    

