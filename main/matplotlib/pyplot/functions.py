import matplotlib.pyplot as plt
import numpy as np

fix, ax = plt.subplots()

# sqrt(x)
X = np.linspace(-5, 5, 100)
Y = np.sqrt(X)
ax.plot(X, Y, label='f(x) = sqrt(x)')

# sqrt(1-x)
X = np.linspace(-5, 5, 100)
Y = np.sqrt(np.ones(100) - X)
ax.plot(X, Y, label='f(x) = sqrt(sqrt(1-x))')

fix, ax = plt.subplots()

# 3x^2
X = np.linspace(-1, 1, 20)
Y = 3*X**2
ax.plot(X, Y, label='f(x) = 3x^2')

# sqrt(1-x^2)
X = np.linspace(-1, 1, 20)
Y = np.sqrt(np.ones(20) - X**2)
ax.plot(X, Y, label='f(x) = sqrt(1-x^2)')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.legend()
plt.show()