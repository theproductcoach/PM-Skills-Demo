# Essentially just using derivatives to find tangent lines.

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2 # our function is y = 2x^2

x = np.arange(0, 50, 0.001) # Our x values, with very small steps to draw the curve
y = f(x) # Plug in x to get the y values

plt.plot(x, y) # Draw the graph

colors = ['k', 'g', 'r', 'b', 'c'] # Adding colors 

def approximate_tangent_line(x, approximate_derivative, b):
    return approximate_derivative*x + b # Simply y = mx + b curve

for i in range(5):
    p2_delta = 0.0001 # Small value to get approx derivative
    x1 = i # Base value to calculate approx derivative
    x2 = x1+p2_delta # This is the second value 2.0001 which is just the small change to get approx derivative

    y1 = f(x1) # Getting the start y coords for the derivative line
    y2 = f(x2) # Getting the end y coords for the derivative line 

    print((x1, y1), (x2, y2))

    approximate_derivative = (y2-y1) / (x2 - x1)
    b = y2 - approximate_derivative*x2 # Calculating the b value (line intersection)

    to_plot = [x1-0.9, x1, x1+0.9] # Range of values for tangent line
    
    plt.scatter(x1, y1, c=colors[i]) # Using the colors to put dots on the graph
    plt.plot(to_plot, [approximate_tangent_line(point, approximate_derivative, b) 
                       for point in to_plot]) # Drawing the tangent line plugging points into approx tangent.

    print('Approximate derivative for f(x)', f'where x = {x1} is {approximate_derivative}') 

plt.show()






