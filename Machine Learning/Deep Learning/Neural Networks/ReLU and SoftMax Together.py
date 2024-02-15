import numpy as np
import nnfs # Make sure you install this in the virtual environment
from nnfs.datasets import spiral_data # Grabbing the nnfs data

nnfs.init()

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons) 
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs): 
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax: # Here we go with the Activation Softmax
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True)) # Back to keeping dimensions and not just grabbing the overall max
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True) # Normalising things again, summing the rows and keeping the dimensions
        self.output = probabilities

X, y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2, 3) # Input data is X, y, output can be anything but we pick 3
activation1 = Activation_ReLU() # Activation function for this layer

dense2 = Layer_Dense(3, 3) # 3 inputs from the last layers' 3 outputs, and 3 neurons for the last layer.
activation2 = Activation_Softmax() # Output layer gets the Softmax activation

dense1.forward(X) # Let's start doing the work - push input data into layer 1
activation1.forward(dense1.output) # Passing layer 1 through the ReLU activation 

dense2.forward(activation1.output) # Passing the layer 1 activation output into layer 2
activation2.forward(dense2.output) # Passing the layer 2 output through the Softmax activation

print(activation2.output[:5]) # The first 5 outputs of the Softmax Activation (all in probabilities)
# [[0.33333334 0.33333334 0.33333334]
#  [0.33331734 0.3333183  0.33336434]
#  [0.3332888  0.33329153 0.33341965]
#  [0.33325943 0.33326396 0.33347666]
#  [0.33323312 0.33323926 0.33352762]]

#  Now it's time to actually train this model! (Loss Functions)
