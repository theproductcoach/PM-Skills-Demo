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