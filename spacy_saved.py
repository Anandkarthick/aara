'''
import ner_update as nau

nau.ner_update("IDENTITY_DOCUMENT")

'''

import random
from pathlib import Path
import spacy

output_dir='model_loc/spy/'
nlp = spacy.load(output_dir)
n_iter=100

TRAIN_DATA = [('send my car id card',{ 'entities': [(12, 18, 'IDENTITY_DOCUMENT')]}),
('send my car insurance identity card', { 'entities': [(12, 34, 'IDENTITY_DOCUMENT') , (12, 21, 'INSURANCE')]}),
('send my auto id card', { 'entities': [(13, 19, 'IDENTITY_DOCUMENT')]}),
('send my auto identity card', { 'entities': [(13, 25, 'IDENTITY_DOCUMENT')]}),
('send my auto insurance card', { 'entities': [(13, 26, 'IDENTITY_DOCUMENT') , (13, 22, 'INSURANCE')]}),
('send auto insurance card', { 'entities': [(10, 23, 'IDENTITY_DOCUMENT') , (10, 19, 'INSURANCE')]}),
('mail my auto insurance identity card', { 'entities': [(13, 35, 'IDENTITY_DOCUMENT') , (13, 22, 'INSURANCE')]}),
('mail my auto insurance card', { 'entities': [(13, 26, 'IDENTITY_DOCUMENT') , (13, 22, 'INSURANCE')]}),
('mail my car insurance id card', { 'entities': [(12, 28, 'IDENTITY_DOCUMENT') , (12, 21, 'INSURANCE')]}),
('send my home id card', { 'entities': [(13, 19, 'IDENTITY_DOCUMENT')]}),
('send my home identity card	', { 'entities': [(13, 25, 'IDENTITY_DOCUMENT')]}),
('send my home insurance card', { 'entities': [(13, 26, 'IDENTITY_DOCUMENT') , (13, 22, 'INSURANCE')]}),
('send my insurance card', { 'entities':	[(8, 21, 'IDENTITY_DOCUMENT') , (8, 17, 'INSURANCE')]})]

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training(lambda: [])
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update( 
                [text],  # batch of texts
                [annotations],  # batch of annotations
                drop=0.5,  # dropout - make it harder to memorise data
                sgd=optimizer,  # callable to update weights
                losses=losses)


# save model to output directory
nlp.to_disk(output_dir)


# test the saved model
#print("Loading from", output_dir)
#nlp2 = spacy.load(output_dir)

