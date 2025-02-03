#import keras
import keras

#import the sequential model
from keras.models import Sequential

#import np for random num
import numpy as np

#import an optimizer (pre-made model optimizer)
#in this example, I imported Stochastic Gradient Descent
from keras.optimizers import SGD

#create a sequential model
model = Sequential()

#model.add(...) to modify model
model.add(keras.layers.Dense(4))
model.add(keras.layers.Dense(4))

#Compiling the model
model.compile(optimizer='sgd', loss='mse', metrics=['accuracy', 'precision'])

#testing model with dummy data
x = np.random.rand(100, 3)
y = np.random.rand(100, 4)

#fitting the model
model.fit(x, y, epochs=10, batch_size=32)