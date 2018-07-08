class tspacy(object):

    def __init__(self, uline):
        self.wdlst = []
        self.cln_str(uline)
    
    def cln_str(self, uline):

        #Loading spacy model
        import spacy
        #nlp = spacy.load('en_core_web_lg')
        output_dir='model_loc/spy'
        nlp = spacy.load(output_dir)

        # removing stop words from the input. 
        doc = nlp(uline)
        in_lst = []
        for token in doc:
            if not token.is_stop:
                if not token.is_punct:
                    in_lst.append(str(token))
        
        strng = " ".join(in_lst)

        doc = nlp(strng)

        for tkn in doc:
            self.wdlst.append(tkn.lemma_)

    
    def return_str(self):
        return self.wdlst


