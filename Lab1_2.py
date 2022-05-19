import numpy as np
 
list1=[1.0,2.0,3.0,4.0,5.0]
npy_array=np.array(list1, dtype=np.float64)
#convert list to array(or something like matrix)
 
npy_array.ndim  # get dimension of array => result = 1
a=np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float64)
# np.array - like creating matrix
a.ndim # number of array dimensions => result = 2
a.shape # return the shape of an array => result = (3, 3)
a.size   # total elem in an array => result = 9
a.itemsize  # each elem's size(in bytes) => result = 8
a.dtype.name  # get elem data type name => result = 'float64'
type(a)   # <class 'ndarray'> ndim array => result = numpy.ndarray
 
np.indices((3,5)) # get index matrix for each elem in 3x5 matrix
# result: array([[[0, 0, 0, 0, 0],
#                 [1, 1, 1, 1, 1],
#                 [2, 2, 2, 2, 2]],
 
#                [[0, 1, 2, 3, 4],
#                 [0, 1, 2, 3, 4],
#                 [0, 1, 2, 3, 4]]])
