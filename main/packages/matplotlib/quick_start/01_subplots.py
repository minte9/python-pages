"""
Simple line
    https://matplotlib.org/stable/tutorials/introductory/quick_start.html
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() # Figure with single axes
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # plot lines
plt.show()

fig, axs = plt.subplots(1, 2) # Figure with 2x2 grid of axes
plt.show()

np.random.seed(100000000)
data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50),
}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fix, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data) # s=size, c=color
ax.set_xlabel('a')
ax.set_ylabel('b')
plt.show()