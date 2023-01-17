import matplotlib.pyplot as plt

# Creating 3 figures
fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()

# Creating subplots in each figure
ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)

# Plotting something in each subplot
ax1.plot([1, 2, 3], [1, 2, 3])
ax2.plot([1, 2, 3], [2, 3, 4])
ax3.plot([1, 2, 3], [3, 4, 5])

plt.show()
