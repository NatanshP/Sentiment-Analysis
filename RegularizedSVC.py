# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:33:40 2016

@author: Natansh
"""

# -*- coding: utf-8 -*-


import pickle
from sklearn import svm
#from sklearn.neural_network import MLPClassifier



features = []

X_file = open('H:\\Python Programs\\ML_PROJECT\\X_final.csv', 'r', encoding = "utf8")

features = [line.split(',') for line in X_file.readlines()]
  
for i in range (0,len(features)):
       x = features[i]
       x.remove('\n')
       features[i] = list(map(int, x))
     
  

X_file.close()


Y_file = open('H:\\Python Programs\\ML_PROJECT\\y_final.csv', 'r')
Y = []
for i in Y_file:
    
    Y.append(int(i.rstrip('\n')))
    
    

Y_file.close()    





X_test = []

X_file = open('H:\\Python Programs\\ML_PROJECT\\X_testfinal.csv', 'r',encoding = "utf8")

X_test = [line.split(',') for line in X_file.readlines()]
  
for i in range (0,len(X_test)):
       x = X_test[i]
       x.remove('\n')
       X_test[i] = list(map(int, x))


       
     
  

        

X_file.close()


Y_file = open('H:\\Python Programs\\ML_PROJECT\\y_testfinal.csv', 'r',encoding = "utf8")
Y_test = []
for i in Y_file:
    
    Y_test.append(int(i.rstrip('\n')))
    
    

Y_file.close()




#from UserSentiment import sentiment_array   
arr = []  
#arr.append(sentiment_array)
print(arr)
#classifier = svm.LinearSVC() 
classifier = svm.SVC(C = 0.75,kernel = 'linear') 
classifier.fit(features,Y)
answers = classifier.predict(X_test) 




#Neural Network

'''
classifier = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(3, 5), random_state=1)
classifier.fit(features,Y)
answers = classifier.predict(X_test) 
'''


result = open('result_final_Regularized.csv' , 'w' )
for i in answers:
    result.write(str(i))
    result.write('\n')
result.close()    

#print(answers)

file = open("classifierfinal_Regularized.pickle",'wb')
pickle.dump(classifier, file)
file.close()




   
    
    
    