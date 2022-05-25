import numpy as np
 
A = np.random.randint(0,2,10)
print("Array A:")
print(A)
 
B = np.random.randint(0,2,10)
print("Array B:")
print(B)
 
array_equal = np.allclose(A, B)
print("Test array A & B equal: " + str(array_equal))
