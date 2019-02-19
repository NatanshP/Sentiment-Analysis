
features = []

X_file = open('H:\\Python Programs\\ML_PROJECT\\X.csv', 'r')

features = [line.split(',') for line in X_file.readlines()]
  


  

for i in range (0,len(features)):
       x = features[i]
       x.remove('\n')
       features[i] = list(map(int, x))
     
print(features)    




Y_file = open('H:\\Python Programs\\ML_PROJECT\\y.csv', 'r')
Y = []
for i in Y_file:
    print(i)
    Y.append(int(i.rstrip('\n')))
print(Y)   
