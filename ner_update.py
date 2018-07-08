class ner_update(object):

    def __init__(self,ner_name):
        self.ner_add(ner_name)

    def ner_add(self, ner_name):
        import spacy

        #Loading existing model to add
        output_dir='model_loc/spy'
        nlp = spacy.load(output_dir)

        #adding new NER to the model
        ner = nlp.get_pipe("ner")
        ner.add_label(ner_name)

        print("New NER added : " + ner_name )

        #saving the model to the disk
        nlp.to_disk(output_dir)