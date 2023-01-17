import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-1, 1, 100) 
I = np.ones(100)

def myfig():
    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    return fig, ax

# sqrt(1+x) / sqrt(1-x)
fig, ax = myfig()
ax.plot(X, np.sqrt(I + X), label='f(x) = sqrt(x)')   
ax.plot(X, np.sqrt(I - X), label='f(x) = sqrt(1-x)')
plt.legend(loc='upper right')
plt.show()

# x^2 / -x^2
fig, ax = myfig()
ax.plot(X,  X**2, label='f(x) = x^2')
ax.plot(X, -X**2, label='f(x) = -x^2')
plt.legend(loc='upper right')
plt.show()