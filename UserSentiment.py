# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:37:11 2016

@author: Natansh
"""
from nltk.tokenize import word_tokenize
import nltk
import pickle
import sys
inp = "this was a bad movie"


'''
file = open("input.txt", 'w')
for i in inp:
    file.write(i)
'''    

classifier_f = open("a_3.pickle","rb")
a = pickle.load(classifier_f)
classifier_f.close()



stoptext = []
file = open('prep.txt', 'r')
for i in file:
    stoptext.append(i.rstrip('\n'))


punct = ['!', ',', '.', '?', '/' , '<', '>','\'','*','\'\'','\\','(',')','--','-',':', '...','***',';',':']

sentiment_array = [0]*len(a)                                           

token = word_tokenize(inp)


iplist = []
input_list = []
for i in range(0,len(token)):
    
    if str(token[i]) == "n't":
        iplist.append("not")
    else:
        iplist.append(token[i].lower())

for i in iplist:
        if i not in stoptext:
            if i not in punct:
               input_list.append(i)
        

for i in range(0,len(input_list)):
        for j in range(0,len(a)):
            
            if input_list[i] == a[j]:
                sentiment_array[j] = 1

               
          
arr = []
arr.append(sentiment_array)
file = open("classifier3.pickle",'rb')
classifier = pickle.load(file)
file.close()
print(classifier.predict(arr)[0] )       

  



