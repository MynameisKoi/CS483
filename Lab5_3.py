import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# create figure and axis objects with subplots()
fig, ax = plt.subplots()

# use numpy to sample 1000 values from the normally distributed random variable with mean 5 and standard deviation 1
x = np.random.normal(5, 1, 1000)

# plot a histogram of the sample probability density
ax.hist(x, bins=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('# of occurrences', color='blue', fontsize=14)

# twin object for two different y-axis on the sample
ax2 = ax.twinx()

# formula for the normal distribution is given by: f(x) = (1/(sqrt(2*pi*sd**2))*exp(-(x-mu)**2/2*sd**2)
# use the formula to generate the shape of a normal distribution that fits the data from x values between 0 and 10
x_fit = np.linspace(0, 10, 100)
y_fit = stats.norm.pdf(x_fit, 5, 1)

# plot a line representing the best fitting normal distribution over the histogram
ax2.plot(x_fit, y_fit, color='red', linewidth=2)
ax2.set_ylabel('% of occurrences', color='red', fontsize=14)

ax2.legend(['Normal Distribution'])
plt.show()
