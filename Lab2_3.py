import numpy as np 
a=np.arange(9) 
b=a.reshape(3,3) 
 
b=a.reshape(5,3) # Error ! no enough element in a 
b.flatten()  # single line array 
b.flatten(order='F')  
# flatten by Fortran language seq. By default, it is C language seq. 
 
a=np.arange(12).reshape(4,3) 
 
np.transpose(a)  
 
b=np.arange(8).reshape(2,4) 
c=b.reshape(2,2,2) 
 
np.rollaxis(c,2,1)  # change row & col  
 
np.swapaxes(c,1,2) 
