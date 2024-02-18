import numpy as np
import nnfs # Make sure you install this in the virtual environment
from nnfs.datasets import spiral_data # Grabbing the nnfs data

nnfs.init()

softmax_outputs = np.array([[0.7, 0.1, 0.2], # Here's our batch of outputs, turned into a np array to make them easier to handle.
                            [0.1, 0.5, 0.4],
                            [0.02, 0.9, 0.08]])

class_targets = [0, 1, 1] # Let's say 0 is a dog and 1 is a cat.

# print(softmax_outputs[[0,1,2], class_targets]) # [0.7 0.5 0.9] Which is 0th from first array, 1st from 2nd, and 1st from 3rd.


neg_log = -np.log(softmax_outputs [ # Wrap the whole thing in an -np.log to calculate losses - [0.35667494 0.69314718 0.10536052]
    range(len(softmax_outputs)), class_targets # Make it more scalable with just using the length of the array. 
]) # If there's a 0 in here everything wigs out, so we need to clip it:

# Clip the 0s:
# y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

average_loss = np.mean(neg_log) # Calculate the average loss (cost)

print(average_loss) # 0.38506088005216804

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons) 
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs): 
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax: 
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True)) 
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True) 
        self.output = probabilities

class Loss: # Calculating loss here, as above.
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss
    
class Loss_CategocialCrossEntropy(Loss): # Categorical cross entropy is the type of loss calculation we're doing.
    def forward(self, y_pred, y_true):
        samples = len(y_pred) # Number of samples we have
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7) # Get rid of those 0s

        if len(y_true.shape) == 1: # Checking for scalar or 1 hot encoding
            correct_confidences = y_pred_clipped[range(samples), y_true]
        
        elif len(y_true.shape) == 2: # This is the 1 hot encoded handling
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1) # This 0s out everything exacpt target class's cofidence.
        
        negative_log_likelihoods = -np.log(correct_confidences) # Just doing the -np.log on those correct confidences to get the 'loss value'
        return negative_log_likelihoods

X, y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2, 3) 
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3, 3) 
activation2 = Activation_Softmax() 

dense1.forward(X) 
activation1.forward(dense1.output) 

dense2.forward(activation1.output) 
activation2.forward(dense2.output) 

print(activation2.output[:5]) 

loss_function = Loss_CategocialCrossEntropy() # Create the function

loss = loss_function.calculate(activation2.output, y) # Pass the Softmax output later activation outputs to the loss calculator (y is still targets)

print("Loss:", loss) #  Loss: 1.0986104

