# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:18:12 2016

@author: Natansh
"""
from sklearn import svm
import pickle

file = open("classifier.pickle",'rb')
classifier = pickle.load(file)
file.close()
classifier.predict()





