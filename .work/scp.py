''' import spacy

nlp = spacy.load('en_core_web_lg')

text = (u"Hey email me my policy"
        u"I would like my auto policy to be sent"
        u"send a copy of my insurance policy"
        u"send policy"
        u"mail me the copy of my policy"
        u"send a copy of the document"
        u"send a copy of my coverage")

text = ("Google is bigger than Apple. Not fruit")

doc = nlp(text)

print(doc)
for token in doc:
    print(token.is_stop)


# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

tk1 = nlp("Insurance needs coverage")
print(tk1.text, tk1.has_vector, tk1.vector_norm)

for token1 in tk1:
    for token2 in tk1:
        print(token1, token2, token1.similarity(token2))

for r in tk1:
    print(r.head) '''

import spacy
import pandas as pd
import string
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
nlp = spacy.load('en_core_web_sm')
punctuations = string.punctuation
def cleanup_text(docs, logging=False):
    texts = []
    counter = 1
    for doc in docs:
        if counter % 1000 == 0 and logging:
            print("Processed %d out of %d documents." % (counter, len(docs)))
        counter += 1
        doc = nlp(doc, disable=['parser', 'ner'])
        tokens = [tok.lemma_.lower().strip() for tok in doc if tok.lemma_ != '-PRON-']
        tokens = [tok for tok in tokens if tok not in stopwords and tok not in punctuations]
        tokens = ' '.join(tokens)
        texts.append(tokens)
    return texts

text = (u"Hey email me my policy"
        u"I would like my auto policy to be sent"
        u"send a copy of my insurance policy"
        u"send policy"
        u"mail me the copy of my policy"
        u"send a copy of the document"
        u"send a copy of my coverage")

doc = nlp("text")
print(cleanup_text(text))