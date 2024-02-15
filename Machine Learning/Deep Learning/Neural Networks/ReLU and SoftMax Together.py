import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X =  [[1, 2, 3, 2.5], # Inputs are usually called 'X'
      [2.0, 5.0, -1.0, 2.0],
      [-1.5, 2.7, 3.3, -0.8]]

X, y = spiral_data(100, 3) # 3 classes, 100 featuresets, each featureset has 2 features

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons) 
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs): 
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

layer1 = Layer_Dense(2, 5)
activation1 = Activation_ReLU()

layer1.forward(X)

# print(layer1.output) #Still has lots of negative values

activation1.forward(layer1.output) # Removing the negatives using our activation function
print(activation1.output)

