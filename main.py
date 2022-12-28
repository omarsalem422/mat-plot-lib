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
