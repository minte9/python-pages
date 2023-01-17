import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^2
def f(x):
    return x**2

# Define the derivative of the function, f'(x) = 2x
def f_derivative(x):
    return 2*x

# Generate x values from -10 to 10 with increments of 0.1
x = np.arange(-10, 10, 0.1)

# Calculate y values for the function f(x) = x^2
y = f(x)

# Calculate y values for the derivative of the function, f'(x) = 2x
y_derivative = f_derivative(x)

# Plot the function f(x) = x^2
plt.plot(x, y, label='f(x) = x^2')

# Plot the derivative of the function, f'(x) = 2x
plt.plot(x, y_derivative, label="f'(x) = 2x", linestyle='--')

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the function f(x) = x^2 and its derivative')
plt.legend()

# Show the plot
plt.show()
