# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:47:51 2016

@author: Natansh
"""
from nltk.tokenize import RegexpTokenizer
import nltk
import random
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from os import listdir
import string
import pickle


stop_words = set(stopwords.words('english'))


#stoptext

stoptext = []
file = open('prep.txt', 'r')
for i in file:
    stoptext.append(i.rstrip('\n'))


file.close()

#stoptext = ['movie','could','``','ca', '\'s','\'ve','has', 'but', 'o', 'under', 'don', 'how', 'll', 'after', 'for', 'themselves', 'yourselves', 'once', 'into', 'too', 'this', 'them', 'will', 't', 'about', 'ours', 'her', 'm', 'i', 'as', 'that', 'had', 'against', 'out', 'any', 'been','ve', 'ourselves', 'theirs', 'have', 'during', 'when', 'weren', 'to', 'and', 'wouldn', 'below', 'mustn', 'myself', 'again', 'ma', 'very', 'd', 'on', 'herself', 'some', 'himself', 'an', 'being', 'him', 'those', 'while', 'just', 'or', 'am', 'having', 'she', 'mightn', 'other', 'does', 'your', 'own', 'over', 'who', 'few', 'through', 'they', 're', 'were', 'than', 'hasn', 'itself', 'are', 'no', 's', 'both', 'such', 'where', 'should', 'aren', 'doing', 'hers', 'there', 'these', 'up', 'in', 'my', 'which', 'it', 'then', 'down', 'why', 'he', 'be', 'each', 'nor', 'with', 'shan', 'ain', 'before', 'more', 'needn', 'at', 'by', 'was', 'of', 'a', 'the', 'its', 'his', 'shouldn', 'what', 'above', 'isn', 'until', 'whom', 'yours', 'all', 'here', 'you', 'same', 'doesn', 'because', 'didn', 'their', 'wasn', 'won', 'most', 'y', 'our', 'haven', 'now', 'do', 'off', 'can', 'me', 'yourself', 'if', 'further', 'is', 'only', 'hadn', 'between', 'from', 'we', 'couldn', 'so', 'did','br']
wordlist = []


for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\neg\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\neg\\'+filename,'r',encoding = "utf-8")
    text = file.read()
    token = word_tokenize(text)
    for word in token:
        if word == "n't":
            wordlist.append("not")
        else:    
            wordlist.append(word.lower())

file.close()       


for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\neg\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\neg\\'+filename,'r',encoding = "utf-8")
    text = file.read()
    token = word_tokenize(text)
    for word in token:
        if word == "n't":
            wordlist.append("not")
        else:    
            wordlist.append(word.lower())

file.close()    
       
for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\pos\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\pos\\'+filename,'r',encoding = "utf-8")
    text = file.read()
    token = word_tokenize(text)
    for word in token:
        if word == "n't":
            wordlist.append("not")
        else:    
            wordlist.append(word.lower())         
file.close()


for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\pos\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\pos\\'+filename,'r',encoding = "utf-8")
    text = file.read()
    token = word_tokenize(text)
    for word in token:
        if word == "n't":
            wordlist.append("not")
        else:    
            wordlist.append(word.lower())         
file.close()



'''
Making prepositions file        
file = open('a.txt','r')


for i in file:
    stoptext.append(i.rstrip('\n'))         
file.close()


file = open('prep.txt' , 'w')
for i in  stoptext:
    file.write(i + '\n' )
file.close()    

'''

'''
file = open('prep.txt', 'w')
for i in stoptext:
    
    file.write(i)
    

file.close()
'''         
 
final_list = []
punct = ['!', ',', '.', '?', '/' , '<', '>','\'','*','\'\'','\\','(',')','--','-',':', '...','***',';',':']
   
for i in wordlist:
     if i not in stoptext:
        if i not in punct:
          final_list.append(i)   
   

    
dist  = nltk.FreqDist(final_list)

#Final_words =  list( dist.keys() )[:10]

# set(final_list)
a = np.array([])
for p in dist:
    if dist[p] > 280:
        a = np.append(a,p.lower())
        
        

    
input_list = []
print(len(a))
file_input = [0]*len(a)

newfile = open('X_final.csv' , 'w')
var_y = open('y_final.csv' , 'w' )

input_wordlist = []

for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\neg\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\neg\\'+filename,'r',encoding = "utf8")
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

for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\neg\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\neg\\'+filename,'r',encoding = "utf8")
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



for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\pos\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\train\\pos\\'+filename,'r',encoding = "utf8")
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

for filename in listdir('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\pos\\'):
    file = open('H:\\Python Programs\\ML_PROJECT\\aclImdb\\test\\pos\\'+filename,'r',encoding = "utf8")
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


print(a)
print(len(a))
save_classifier = open("a_final.pickle","wb")
pickle.dump(a, save_classifier)
save_classifier.close()




 





























#print(len(set(final_list)))    

    
    
    
    
    
    