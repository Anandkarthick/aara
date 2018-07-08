import tspacy as tp
import spacy

output_dir='model_loc/spy'
nlp = spacy.load(output_dir)

ph = "Please send my insurance id card"

result = str(tp.tspacy(ph).return_str())

doc = nlp(result)

for ent in doc.ents:
    print(ent.text, ent.label_)



