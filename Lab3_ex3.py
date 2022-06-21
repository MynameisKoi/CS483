#Use this definition to plot the shape of a limacon for 𝑟0 = 0.8, 𝑟0 = 1.0, and 𝑟0 = 1.2
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

image = plt.figure(figsize=(16,10), dpi= 200)
theta = np.arange(-5,5,0.001)

#Change r0 from 0.8, 1, to 1.2
r0_1 = 0.8
r1 = r0_1 + np.cos(theta)
x1 = r1*np.cos(theta)
y1 = r1*np.sin(theta)

r0_2 = 1
r2 = r0_2 + np.cos(theta)
x2 = r2*np.cos(theta)
y2 = r2*np.sin(theta)

r0_3 = 1.2
r3 = r0_3 + np.cos(theta)
x3 = r3*np.cos(theta)
y3 = r3*np.sin(theta)

#Plot the three limacons
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x1, y1, label = 'r0 = 0.8')
plt.plot(x2, y2, label = 'r0 = 1')
plt.plot(x3, y3, label = 'r0 = 1.2')


# include a legend explaining which line is which plot
plt.legend(['r0 = 0.8', 'r0 = 1', 'r0 = 1.2'], prop={'size': 15})
image.show()

#Save plot as a pdf file
image.savefig('cs483_lab3_ex3.pdf')
files.download('cs483_lab3_ex3.pdf')
