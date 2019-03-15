%matplotlib inline

import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import matplotlib.pyplot as plt
import numpy as np
import os

clear = lambda: os.system('cls')

def training():
    mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
    (x_train, y_train),(x_test, y_test) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train/y_test

    x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1
    x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1

    model = tf.keras.models.Sequential()  
    model.add(tf.keras.layers.Flatten(input_shape=x_train[0].shape))  # takes our 28x28 and makes it 1x784
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

    model.compile(optimizer='adam',  # Good default optimizer to start with
                loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
                metrics=['accuracy'])  # what to track

    model.fit(x_train, y_train, epochs=3)  # train the model

    model.save('class_model.model')

    val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
    predictions = model.predict([x_test])
    #print(val_loss)  # model's loss (error)
    print(val_acc*100)  # model's accuracy
    return x_test, predictions

if os.path.isfile('class_model.model'):
    print("Van már egy előre trainelt modell, akarod használni? [I/N]")
    if input().upper() == "I":
        model = tf.keras.models.load_model('class_model.model')
        mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
        (x_train, y_train),(x_test, y_test) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train/y_test

        x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1
        x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1
        val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
        predictions = model.predict([x_test])
        #print(val_loss)  # model's loss (error)
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
    
