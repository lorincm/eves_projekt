%matplotlib inline

import tensorflow as tf  
import matplotlib.pyplot as plt
import numpy as np
import os

clear = lambda: os.system('cls')

def training():
    mnist = tf.keras.datasets.mnist 
    (x_train, y_train),(x_test, y_test) = mnist.load_data()  

    x_train = tf.keras.utils.normalize(x_train, axis=1)  
    x_test = tf.keras.utils.normalize(x_test, axis=1)  

    model = tf.keras.models.Sequential()  
    model.add(tf.keras.layers.Flatten(input_shape=x_train[0].shape))  
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) 
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  

    model.compile(optimizer='adam',  
                loss='sparse_categorical_crossentropy',  
                metrics=['accuracy']) 

    model.fit(x_train, y_train, epochs=3)  

    model.save('class_model.model')

    val_loss, val_acc = model.evaluate(x_test, y_test) 
    predictions = model.predict([x_test])
    #print(val_loss) 
    print(val_acc*100)  
    return x_test, predictions

if os.path.isfile('class_model.model'):
    print("Van már egy előre trainelt modell, akarod használni? [I/N]")
    if input().upper() == "I":
        model = tf.keras.models.load_model('class_model.model')
        mnist = tf.keras.datasets.mnist  
        (x_train, y_train),(x_test, y_test) = mnist.load_data()  

        x_train = tf.keras.utils.normalize(x_train, axis=1) 
        x_test = tf.keras.utils.normalize(x_test, axis=1) 
        val_loss, val_acc = model.evaluate(x_test, y_test) 
        predictions = model.predict([x_test])
        #print(val_loss) 
        print(val_acc*100)
else:
    x_test, predictions = training()

while True:
    testify=input()
    testify=int(testify)
    clear()
    plt.imshow(x_test[testify], cmap = plt.cm.gist_gray)
    plt.show()
    print(np.argmax(predictions[testify]))
    
