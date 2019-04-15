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
    for t in range(100):
        data = npdata[t]

        z = data[0] * w[0] + data[1] * w[1] + data[2] * w[2] + data[3] * w[3] + b
        pred = sigmoid(z)

        cost = (pred - data[4])**2 #a data[4] tartalmazza a cél értéket

        dcost = 2 * (pred - data[4]) #a data[4] tartalmazza a cél értéket

        dz_cost = dcost * dsigmoid(z)
        
        w[0] -= learning_rate * (dz_cost * data[0])
        w[1] -= learning_rate * (dz_cost * data[1])
        w[2] -= learning_rate * (dz_cost * data[2])
        w[3] -= learning_rate * (dz_cost * data[3])
        b    -= learning_rate * (dz_cost * 1)
        
        if(i==100 and t==1 or i==9999 and t==1): #debug
            print(w[0], w[1], w[2], w[3], b)
            
test = [5.1, 3.5, 1.4, 0.2]

z = test[0] * w[0] + test[1] * w[1] + test[2] * w[2] + test[3] * w[3] + b
print(sigmoid(z))
