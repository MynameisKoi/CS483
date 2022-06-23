# 1. Subplots
import random
import matplotlib.pyplot as plt
from matplotlib import style
# %matplotlib notebook
style.use('fivethirtyeight') # Style w/o borders in the plot
fig = plt.figure()
def create_plots():
    xs = []
    ys = []
    
    for i in range(10):
        x = i
        y = random.randrange(10)
        
        xs.append(x)
        ys.append(y)
    return xs, ys
ax1 = plt.subplot2grid((6,1),(0,0), rowspan = 1, colspan = 1)
ax2 = plt.subplot2grid((6,1),(1,0), rowspan = 4, colspan = 1)
ax3 = plt.subplot2grid((6,1),(5,0), rowspan = 1, colspan = 1)
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,1,2)
x,y = create_plots()
ax1.plot(x,y)
x,y = create_plots()
ax2.plot(x,y)
x,y = create_plots()
ax3.plot(x,y)
plt.show()

# 2. 3D graphs with Matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
figure = plt.figure()
axis = figure.add_subplot(111, projection = '3d')
x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = np.array([[1,2,6,3,2,7,3,3,7,2],[1,2,6,3,2,7,3,3,7,2]])
axis.plot_wireframe(x, y, z)
axis.set_xlabel('x-axis')
axis.set_ylabel('y-axis')
axis.set_zlabel('z-axis')
plt.show()

# 3. 3D Scatter Plot with Matplotlib
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d') # same as subplot(1,1,1)
x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]
x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [1,2,6,3,2,7,3,3,7,2]
ax1.scatter(x, y, z, c='g', marker='o')
ax1.scatter(x2, y2, z2, c ='r', marker='o')
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()

# 4. 3D Bar Chart with Matplotlib
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,7,8,2,5,6,3,7,2]
z3 = np.zeros(10)
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]
ax1.bar3d(x3, y3, z3, dx, dy, dz)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()

# 5. Conclusion
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
# %matplotlib notebook
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1, projection = '3d')
x, y, z = axes3d.get_test_data()
# print(axes3d.__file__)
ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()
