class linear_svc_test(object):

    def __init__(self, Xtest_data):
        self.predict(Xtest_data)

    def predict(self, xtest_ph):
        import pickle
        from sklearn.feature_extraction.text import CountVectorizer

        filename = 'model_loc/linearSVC_countvec.pkl'
        cv=pickle.load(open(filename, 'rb'))
        print(xtest_ph)
        y_data = cv.transform([xtest_ph])
        s=pickle.load(open('model_loc/linearSVC.pkl','rb'))

        result = s.predict(y_data)

        #sprob = s.predict_proba(y_data)
        
        #print(s.predict_log_proba(y_data))

        #print(s.score(xtest_ph,y_data))
        
        print(result)

        #print(sprob)

