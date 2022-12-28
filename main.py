# Matplotlib Tutorial Series

# Import relevant modules
import matplotlib.pyplot as plt
import numpy as np

# Creating simple arrays
x = np.array([0,100])
y = np.array([0,4])

# Plotting x and y - a simple line
# The first argument in the x-axis and the second argument
# is the y-axis

plt.plot(x,y)
plt.show()
# You always need to write plt-show() in order to see the graph
# plt-show()  # this shows the graph

# Plotting several points in matplotlib
# Each numpy array has to be the same length
x = np.array([0, 30, 12, 56, 19, 100])
y = np.array([40, 72, 80, 13, 17, 39])

# Instead of a line graph we want a scatter graph
# Method #1
plt.plot(x, y, 's')
plt.show()

# Method #2
plt.scatter(x, y)
plt.show()

# Metplotlib's degault x and y axis
a = np.array([0, 10, 20, 30, 100, 30, 50, 100])

plt.plot(a)
plt.show()