# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:56:12 2016

@author: Natansh
"""

from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
example_text = "what are you doing?"

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

word_tokenize(example_text)

words = word_tokenize(example_text)
#ps.stem()
filtered_sentence = []
for w in words :
    if w not in stop_words:
        filtered_sentence.append(w)
        
        
        
        ''''
        pickling
        
        import pickle
        save_classifier = open("filenam.pickle","wb")
        pickle.dump(classifier, save_classifier)
        save_classifier.close
        classifier_f = open("filename.pickle","rb")
        classifier = pickel.load(classifier_f)
        classifier_f.close
        
        