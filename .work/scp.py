import spacy

nlp = spacy.load('en_core_web_sm')
text = (u"Hey email me my policy"
        u"I would like my auto policy to be sent"
        u"send a copy of my insurance policy"
        u"send policy"
        u"mail me the copy of my policy"
        u"send a copy of the document"
        u"send a copy of my coverage")

doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

