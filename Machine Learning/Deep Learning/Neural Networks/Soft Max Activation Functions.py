# This activation function is for output layers.
# We need to figure out how 'wrong' the output layer data points are
# If we use ReLU then we're clipping values at 0 and negatives and have no way of knowing how wrong we were
# So we're going to use a different function that uses exponentiation instead.

import math 

layer_outputs = [4.8, 1.21, 2.385]

E = math.e # This is easier than typing the constant.

# E = 2.71828182846 # eulers constant

exp_values = []

for output in layer_outputs: #For each of our outputs lets exponentiate with eulers number.
    exp_values.append(E**output)

print (exp_values) # [121.51041751873483, 3.353484652549023, 10.859062664920513] The values

# Now we have to normalise the values (to get probability distributions)
    
norm_base = sum(exp_values) # Bottom of the fraction is exponentiated values
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base) # Normalising by dividing the original value by the base

print(norm_values) # [0.8952826639572619, 0.024708306782099374, 0.0800090292606387] The normalised values

print(sum(norm_values)) # 0.9999999999999999 Proof that the normalised valued add up to ~1 (0.999... = 1)

# Now let's do this with numpy:

import numpy as np

layer_outputs = [4.8, 1.21, 2.385]

E = math.e

exp_values = np.exp(layer_outputs) # Exponentiates the output values [121.51041752   3.35348465  10.85906266]

print(exp_values) 
    
norm_values = exp_values / np.sum(exp_values)

print(norm_values) # [0.89528266 0.02470831 0.08000903]
print(sum(norm_values)) # 0.9999999999999999

# So overall what we're doing:
# Input --> Exponentiate --> Normalise --> Output
# In other words Input --> SoftMax --> Output

# Let's conver the layer_outputs to a batch to work with more realistic data

layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.42, 1.051, 0.026]]

exp_values = np.exp(layer_outputs)

print(exp_values) # Can see that it's done all of the values
# [[1.21510418e+02 3.35348465e+00 1.08590627e+01]
# [7.33197354e+03 1.63654137e-01 1.22140276e+00]
# [4.13712044e+00 2.86051020e+00 1.02634095e+00]]

# print(np.sum(layer_outputs)) # Just adds everything (18.182000000000002), we want 3 values

# print(np.sum(layer_outputs, axis=0)) # Axis 0 sums columns ([15.12   0.451  2.611]) but we want rows

# print(np.sum(layer_outputs, axis=1)) # Axis 0 does the rows ([8.395 7.29  2.497]) But we still need to shape this so that it does the order of operations and matrix multiply properly

print(np.sum(layer_outputs, axis=1, keepdims=True)) # This gives us the sums in an array of arrays (list of lists):
# [[8.395]
#  [7.29 ]
#  [2.497]]

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True) # Now this should work.

print(norm_values) # Here's our normalised Values
# [[8.95282664e-01 2.47083068e-02 8.00090293e-02]
#  [9.99811129e-01 2.23163963e-05 1.66554348e-04]
#  [5.15595101e-01 3.56495554e-01 1.27909345e-01]]

# Now the actual SoftMax part is basically taking the largest value in the set and subtracting that form everything.
# Why? So we can limit memory problems with large number exponentiation, if it gets too big too quickly (which it tends to do) it'll blow things up.

