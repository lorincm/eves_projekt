import numpy   as np
import pandas  as pd

pd.options.mode.chained_assignment = None

csv = pd.read_csv("iris.csv", sep=",")
csv.species[csv.species == "Iris-setosa"]         = 0
csv.species[csv.species == "Iris-versicolor"]     = 1

npdata=csv.values

def sigmoid(z):
    return 1/(1+np.exp(-z))

def dsigmoid(z):
    return sigmoid(z) * (1-sigmoid(z))

w = [np.random.randn(), np.random.randn(), np.random.randn(), np.random.randn()]
b = np.random.randn()

learning_rate = 0.1

for i in range(10000):
    for t in range(90):
        tdata = npdata[t]

        z = tdata[0] * w[0] + tdata[1] * w[1] + tdata[2] * w[2] + tdata[3] * w[3] + b
        pred = sigmoid(z)

        cost = (pred - tdata[4])**2 #a data[4] tartalmazza a cél értéket

        dcost = 2 * (pred - tdata[4]) #a data[4] tartalmazza a cél értéket

        dz_cost = dcost * dsigmoid(z)
        
        w[0] -= learning_rate * (dz_cost * tdata[0])
        w[1] -= learning_rate * (dz_cost * tdata[1])
        w[2] -= learning_rate * (dz_cost * tdata[2])
        w[3] -= learning_rate * (dz_cost * tdata[3])
        b    -= learning_rate * (dz_cost * 1)
        
        if(i==100 and t==1 or i==9999 and t==1): #debug
            print(w[0], w[1], w[2], w[3], b)
            

#testing
csv = pd.read_csv("test.csv", sep=",")
csv.species[csv.species == "Iris-setosa"]         = 0
csv.species[csv.species == "Iris-versicolor"]     = 1

npdata=csv.values

for i in range(10):
    test = npdata[i]
    z = test[0] * w[0] + test[1] * w[1] + test[2] * w[2] + test[3] * w[3] + b
    print(str(test[4])+", értékhez tartozó jóslat: "+str(sigmoid(z)))
