# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 22:32:03 2016

@author: Natansh
"""

from nltk.tokenize import RegexpTokenizer
import nltk
import random
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from os import listdir
import pickle


classifier_f = open("a_final.pickle","rb")
a = pickle.load(classifier_f)
classifier_f.close


stoptext = []
file = open('prep.txt', 'r')
for i in file:
    stoptext.append(i.rstrip('\n'))



    
input_list = []
input_wordlist = []
file_input = [0]*len(a)

print(len(a))

punct = ['!', ',', '.', '?', '/' , '<', '>','\'','*','\'\'','\\','(',')','--','-',':', '...','***',';',':']



newfile = open('X_testfinal.csv' , 'w')
var_y = open('y_testfinal.csv' , 'w' )








for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\neg_test\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\neg_test\\'+filename,'r',encoding = "utf8")
    
    try:    
     text = file.read()
     token = word_tokenize(text)
     for word in token:
         if word == "n't":
             input_wordlist.append("not")
         else:    
             input_wordlist.append(word.lower())
     for i in input_wordlist:
#        print('.')
        if i not in stoptext:
            if i not in punct:
               input_list.append(i)                                            
     for i in range(0,len(input_list)):
#        print('.')
        for j in range(0,len(a)):
            if input_list[i] == a[j]:
                file_input[j] = 1
                    
     for i in file_input:
        newfile.write(str(i) + ',' )
     var_y.write('0' + '\n')    
     newfile.write('\n')    
     file_input = [0]*len(a)
     input_wordlist = []
     input_list = []
        
    except :
         print('err')
         
         

for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\pos_test\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\pos_test\\'+filename,'r',encoding = "utf8")
    text = file.read()
    token = word_tokenize(text)
    for word in token:
         if word == "n't":
             input_wordlist.append("not")
         else:    
             input_wordlist.append(word.lower())
    for i in input_wordlist:
#        print('.')
        if i not in stoptext:
            if i not in punct:
               input_list.append(i)                                            
    for i in range(0,len(input_list)):
#        print('.')
        for j in range(0,len(a)):
            if input_list[i] == a[j]:
                file_input[j] = 1
    for i in file_input:
        newfile.write(str(i) + ',' )
    var_y.write('1' + '\n')    
    newfile.write('\n')    
    file_input = [0]*len(a)
    input_wordlist = []
    input_list = []

                

newfile.close()
var_y.close() 

print('done!')
