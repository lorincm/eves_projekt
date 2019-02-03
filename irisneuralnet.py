import numpy   as np
import pandas  as pd

csv = pd.read_csv("C:\\Users\\louvre\\Desktop\\iris.csv", sep=",")
csv.species[csv.species == "Iris-setosa"]         = 0
csv.species[csv.species == "Iris-versicolor"]     = 1

npdata=csv.values

def sigmoid(z):
    return 1/(1+np.exp(-z))

def dsigmoid(z):
    return sigmoid(z) * (1-sigmoid(z))

w1  = np.random.randn()
w2  = np.random.randn()
w3  = np.random.randn()
w4  = np.random.randn()
b   = np.random.randn()

learning_rate = 0.1

for i in range(10000):
    for t in range(100):
        data = npdata[t]

        z = data[0] * w1 + data[1] * w2 + data[2] * w3 + data[3] * w4 + b
        pred = sigmoid(z)

        target = data[4]

        cost = (pred - target)**2

        dcost = 2 * (pred - target)
        dz_sig = dsigmoid(z)

        dz_dw1 = data[0]
        dz_dw2 = data[1]
        dz_dw3 = data[2]
        dz_dw4 = data[3]
        dz_db = 1

        dz_cost = dcost * dz_sig
        
        dcost_dw1 = dz_cost * dz_dw1 
        dcost_dw2 = dz_cost * dz_dw2
        dcost_dw3 = dz_cost * dz_dw3
        dcost_dw4 = dz_cost * dz_dw4
        dcost_db  = dz_cost * dz_db

        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        w3 = w3 - learning_rate * dcost_dw3
        w4 = w4 - learning_rate * dcost_dw4
        b  = b - learning_rate * dcost_db

test = [5.1, 3.5, 1.4, 0.2]

z = test[0] * w1 + test[1] * w2 + test[2] * w3 + test[3] * w4 + b
pred = sigmoid(z)

print(pred)
