import matplotlib.pyplot as plt
import numpy as np

# use numpy to generate a vector 'x' of 100 values between 0 and 10
x = np.linspace(0, 10, 100)

# generate a vector 'y' from x using a regression y = 2x + e, where e is a gaussian random variable with mean 0 and standard deviation 1
y = 2*x + np.random.normal(0, 1, 100)

# use matplotlib.pyplot to plot the scatter graph of x and y
plt.scatter(x, y)

# include labels for the x and y axes
plt.xlabel('x')
plt.ylabel('y')

# include a title and a legend for the plot
plt.title('Scatter Plot')
plt.legend(['y = 2x + e']) 

# use matplotlib to add the correct regression line y = 2x 
plt.plot(x, 2*x)
plt.show()
