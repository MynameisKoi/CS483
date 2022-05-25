import numpy as np

a=np.array([[1,2],[3,4]]) 
b=np.array([[5,6],[7,8]])  
np.concatenate((a,b))    # Join by col 
np.concatenate((a,b), axis=1)  # Join by row 
