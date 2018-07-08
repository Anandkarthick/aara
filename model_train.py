class model_train(object):

    def selection(self):
        print(self.ft_name, "Feature selected")

    def load_file(self, ft_name):
        import pandas as pd
        temp_var = 'train/'+ft_name+'.csv'
        test_df = pd.read_csv(temp_var)
        category_corpus = test_df['content']
        Y_train_data = test_df['content_feature']
        self.model_fit(category_corpus,Y_train_data)
        #return(self.selection())

    def __init__(self, ft_name):
        self.ft_name=ft_name
        self.selection()
        self.load_file(ft_name)
    
    def model_fit(self, Xtrain_df, Ytrain_df):
        # Use CountVectorizer to calculate word frequency & to use IDF to calculate weights for the features.
        import warnings
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.feature_extraction.text import TfidfTransformer
        from sklearn.naive_bayes import MultinomialNB
        import pickle   
        import os

        warnings.simplefilter(action='ignore', category=FutureWarning)

        count_vect = CountVectorizer(stop_words='english')
        print("Count Vector process started.. ")
        X_train_count = count_vect.fit_transform(Xtrain_df)
        print(count_vect.inverse_transform(X_train_count))
        print("\n Count Vector process completed.. ")

        tfitd_weight = TfidfTransformer()
        X_train_weight = tfitd_weight.fit_transform(X_train_count)
        print("\n IDF process completed.. ")
        print(X_train_weight.shape)

        # Check.. Shape of the X & Y axis

        print(X_train_weight.shape)
        print(Ytrain_df.shape)

        print("Fitting the model.. Multinomial NB")

        clf = MultinomialNB()
        clf.fit(X_train_weight, Ytrain_df)

        print("Model trained.. Let's pickle the model in and see some metrics.")

        filename = 'model_loc/multiNB_countvec.pkl'
        pickle.dump(count_vect, open(filename, 'wb'))

        filename = 'model_loc/multiNB.pkl'
        pickle.dump(clf, open(filename, 'wb'))

        print("model saved..")

        from sklearn.metrics import accuracy_score

        print(clf.score(X_train_weight, Ytrain_df))

