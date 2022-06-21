# Use matplotlib.pyplot to produce a plot of the functions f(x) = e^(-x/10) and g(x) = xe^(-x/3)
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

image = plt.figure(figsize=(16,10), dpi= 200)
x = np.arange(0, 10, 0.1)
f = np.exp(-x/10)
g = x*np.exp(-x/3)

# include labels for the x and y axes
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, f, label='f(x)')
plt.plot(x, g, label='g(x)')

# include a legend explaining which line is which plot
plt.legend(['f(x)', 'g(x)'], prop={'size': 25})
image.show()

# save the plot as a jpeg file
image.savefig('cs483_lab3_ex2.jpg',  bbox_inches="tight")
files.download('cs483_lab3_ex2.jpg')
