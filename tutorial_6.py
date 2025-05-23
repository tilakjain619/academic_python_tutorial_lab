#Implement a program to plot error bars on a line or scatter plot to represent uncertainity in data. Demonstrate how to customize error bars and visualize confidence intervals.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.log(x)
error = 0.2 * y

plt.errorbar(x, y, yerr=error, fmt='o', capsize=4, color='blue')
plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)
ci = 0.2

plt.plot(x, y, color='green')
plt.fill_between(x, y - ci, y + ci, color='green', alpha=0.2)
plt.show()