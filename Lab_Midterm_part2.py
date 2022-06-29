import matplotlib.pyplot as plt

# plot two lines on one figure with the legend for each
x = [1,2,3,4,5,6,7,8,9]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.legend(['y = x^2', 'y = x^3'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Draw a 2d scatter plot for samples (X1, X2, y) in different colors for y = 0 and y = 1 
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
x1 = [-3.98, -3.464, -3.461, -2.22, -2.02, -2.01, -1.42, -1.416, -1.09, -0.19, 0.01, 0.03, 0.04, 0.06, 0.07, 0.12, 1.11, 1.411, 1.414, 1.86, 1.96, 2.11, 3.461, 3.464, 4.12]
x2 = [-0.12, -2.11, 1.89, -3.474, 0.03, 3.459, -1.409, 1.419, 0.08, -4.13, 1.02, -2.12, 2.06, 3.97, 0.1, -1.12, 0.09, 1.419, -1.415, 3.47, -0.12, -3.472, -1.87, 2.07, 0.09]
y = [1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1]

# if y = 0, the color is blue
# if y = 1, the color is red
# plot all x1, x2 points with color for y = 0 and y = 1
s = plt.scatter(x1, x2, c=y ,cmap = mcolors.ListedColormap(["blue", "red"]),marker='o')

# include legend for red and blue points
h, l = s.legend_elements()
plt.legend(h,("y = 0", "y = 1"))

plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
