import numpy as np 
import matplotlib.pyplot as plt 
 
x=np.linspace(-4,4,9) 
y=np.linspace(-5,5,11) 
 
xx,yy=np.meshgrid(x,y)  # create x, y grid matrix 
 
xx.shape 
yy.shape 
 
ellipse = xx**2 + 4*yy**4 # 
 
plt.contourf(xx,yy,ellipse, cmap='jet') # generate contour line 
    # 'jet': Red for big value; Blue for small value 
plt.colorbar()    # create color bar at the side 
plt.show() 
 
random_data=np.random.random((11,9)) 
plt.contourf(xx,yy,random_data, cmap='jet') # generate contour line 
    # jet - color seq:blue-cyan-yello-red 
plt.colorbar()    # create color bar at the side 
plt.show() 
 
 
xx1,yy1=np.meshgrid(x,y, indexing='ij')  
# xx1 is transpose xx; yy1 is transpose yy 
np.all(xx == xx1.T) # xx1.T - transpose matrix  
#True  # if all elem in expression are the same return np.all(yy == yy1.T) 
#True 
 
# e.g.  
np.all([1,2] == [1,3]) 
False 
