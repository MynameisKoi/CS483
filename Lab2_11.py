import numpy as np 
import matplotlib.pyplot as plt 
 
x=np.arange(0,3*np.pi,0.1) 
y=np.sin(x) 
plt.plot(x,y) 
plt.show() 
 
# Create a 6x6 2-dim array, and let 1 and 0 be placed alternatively across the diagonals 
 
z=np.zeros((6,6),dtype=int)) 
z[1::2, ::2] = 1 # 1st:last:step 
 
z[::2, 1::2] = 1 # 1st:last:step 
 
# Find the total number and locations of missiong values in the array 
z=np.random.rand(10,10) 
z[np.random.randint(10, size=5), np.random.randint(10, size=5)]=np.nan 
# np.random.randint(10, size=5) return array with 5 elem from 1 to 10 
# z[[],[]] for elem index 
np.isnan(z).sum() 
np.argwhere(np.isnan(z)) 
 
inds=np.where(np.isnan(z)) # return ind array 
 
z[inds]=0 
