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

# Markers in matplotlib
x = np.array([0, 1, 2, 3, 4])
y = np.array([20, 30, 50, 100, 101])

plt.plot(x, y, marker='s')
plt.show()

# Change the color and line reference of graphs!
# There are so many different colors and linestyles!
# Just google them to a play around
x = np.array([0, 1, 2, 3, 4])
y = np.array([20, 30, 50, 100, 101])

# Markersize - markersize=10 (simplified to ms)
# Marker color - markerfacecolor="blue"
# Marker edge color - markeredgecolor="blue"
plt.plot(x, y, c='black', marker='*', linestyle='--', markersize=10, markerfacecolor='blue',
         markeredgecolor='blue', linewidth=2)
plt.show()

# PLotting more than one graph on a plot - actually 3 plots!
x = np.array([0, 10, 100])
y = np.array([0, 1, 2])
plt.plot(x,y)

r = np.array([0, 50, 10])
s = np.array([0, 46, 92])
plt.plot(r,s)

a = np.array([0, 80, 100])
b = np.array([0, 40,92])
plt.plot(a,b)
plt.show()