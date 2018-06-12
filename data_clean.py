class data_clean(object):

    def return_str(self):
        return self.result_val

    def cleanup(self,phrase):
        print(phrase)
        from sklearn.feature_extraction.text import CountVectorizer
        count_vect = CountVectorizer(stop_words='english')
        print("Count Vector process started.. ")
        vectr = count_vect.fit_transform([phrase])
        #print(vectr)
        #print(count_vect.vocabulary_)
        #print(count_vect.stop_words_)
        self.result_val = " ".join(count_vect.inverse_transform(vectr)[0])
        #print(result_str)
        ##print(type(result_str))
        #return (count_vect.inverse_transform(vectr)[0])


    def __init__(self, phrase):
        self.result_val = " "
        self.cleanup(phrase)
    
