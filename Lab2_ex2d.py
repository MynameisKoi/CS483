import numpy as np

#Calculate the time of both sum function for a small array
array = np.random.random(10)
 
%timeit sum(array) #Python sum
%timeit np.sum(array) #Numpy sum

#Calculate the time of both sum function for a large array
array = np.random.random(10000)
 
%timeit sum(array) #Python sum
%timeit np.sum(array) #Numpy sum
