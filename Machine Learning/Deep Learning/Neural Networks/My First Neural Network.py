
# Inputs from the last layer
inputs = [1, 2, 3, 2.5] 

weights = [[0.2, 0.8 ,-0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]


# Calculate the output of the neuron
layer_outputs = [] # Output of the current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Output of a given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)


# Learning dot products
import numpy as np

inputs = [1, 2, 3, 2.5] 

weights = [[0.2, 0.8 ,-0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]

output = np.dot(weights, inputs) + bias

print(output)


# Let's Batch Inputs

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8 ,-0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output = np.dot(inputs, np.array(weights).T) + biases # Adding transpose to make sure the shapes are right

print(output)

# Addinng another layer

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8 ,-0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

weights2 = [[0.1, -0.14, 0.5], 
           [-0.5, 0.12, -0.33], 
           [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases # Adding transpose to make sure the shapes are right

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2 # Adding transpose to make sure the shapes are right


print(layer2_outputs)

# Let's start using Objects

import numpy as np

np.random.seed(0)

X =  [[1, 2, 3, 2.5], # Inputs are usually called 'X'
      [2.0, 5.0, -1.0, 2.0],
      [-1.5, 2.7, 3.3, -0.8]]

# As we initialise the values we want to use 'small' values between -1 and 1 so that the weights later on don't blow the values up. 
# For Biases we tend to initialise those as 0. Be careful that we don't kill the network by multiplying things by 0 though (might require initialising at non-0)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons) #Initialise weights with a normal distribution, multiplying by 0.10 to get smaller values.
        self.biases = np.zeros((1, n_neurons)) # Initialise an array of 0's with the shape of 1, and n_neurons i.e. [0, 0, 0...etc]
    def forward(self, inputs): 
        self.output = np.dot(inputs, self.weights) + self.biases # Output calculation using inputs, weights, and biases (matrix multiply through np.dot)

layer1 = Layer_Dense(4, 5) # Size of inputs (i.e. 4 samples in the input), and how many neurons we want to have.
layer2 = Layer_Dense(5, 2) # Input has to be the shape of the output of layer1, output can be anything.

layer1.forward(X) # Sending X data through layer 1

print(layer1.output)

layer2.forward(layer1.output) # Sending layer1 output data through layer 2

print(layer2.output)




