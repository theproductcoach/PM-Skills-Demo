
# Inputs from the last layer
# inputs = [1, 2, 3, 2.5] 

# weights = [[0.2, 0.8 ,-0.5, 1], 
#            [0.5, -0.91, 0.26, -0.5], 
#            [-0.26, -0.27, 0.17, 0.87]]

# biases = [2, 3, 0.5]


# # Calculate the output of the neuron
# layer_outputs = [] # Output of the current layer
# for neuron_weights, neuron_bias in zip(weights, biases):
#     neuron_output = 0 # Output of a given neuron
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_output += n_input*weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)

# print(layer_outputs)


# # Learning dot products
# import numpy as np

# inputs = [1, 2, 3, 2.5] 

# weights = [[0.2, 0.8 ,-0.5, 1], 
#            [0.5, -0.91, 0.26, -0.5], 
#            [-0.26, -0.27, 0.17, 0.87]]

# bias = [2, 3, 0.5]

# output = np.dot(weights, inputs) + bias

# print(output)


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

weights2 = [[0.2, 0.8 ,-0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases2 = [2, 3, 0.5]

output = np.dot(inputs, np.array(weights).T) + biases # Adding transpose to make sure the shapes are right

print(output)






