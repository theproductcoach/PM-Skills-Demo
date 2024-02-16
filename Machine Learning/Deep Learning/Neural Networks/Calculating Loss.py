import math

# We're using a process called 'categorical cross entropy' and 'one hot encoding'

# Remember that the softmax output is the confidence in that output being correct (from 0-1) and we're calculating how 'wrong' that is

softmax_output = [0.7, 0.1, 0.2] # Example output from softmax activation function
target_output = [1, 0 ,0 ]

# target_class = 0 # We want the output for the class to be 0 (instead of 1)

loss = -(math.log(softmax_output[0]) * target_output[0] + # Calculate the loss by using natural logs times output value (2 are 0) 
         math.log(softmax_output[1]) * target_output[1] + 
         math.log(softmax_output[2]) * target_output[2])

print(loss)

# We could simplify the loss function to look like this:

loss = -(math.log(softmax_output[0]))

print(loss)

# Replacing the 'softmax_output' part of the calculation to demonstrate how loss goes up

loss = -(math.log(0.7)) # Here's a 0.7 confidence level
print(loss)  # 0.35667494393873245 loss value

loss = -(math.log(0.5)) # Here's a 0.5 confidence level
print(loss) # 0.6931471805599453 much bigger loss value