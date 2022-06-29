import numpy as np

# create 3x3 matrix with random integer numbers
print("Create 3x3 matrix with random numbers")
A = np.random.randint(0, 30, size=(3, 3))
print(A)

# don't change original array, substitute even numbers in it to -1
print("Substitute even numbers in an array to -1")
a = [11, 12, 13, 14]
b = []
for i in range(len(a)):
  if a[i] % 2 == 0:
    b.append(-1)
  else:
    b.append(a[i])
print("a = ", a)
print("b = ", b)

# extract the common elements in two arrays
print("Extract the common elements in two arrays")
a = [11,12,13,14]
b = [11,13,15,16]
c = []
for i in a:
    if i in b:
        c.append(i)
print("c = ", c)

# swap 2 rows in a 3x3 matrix
print("Swap 2 rows in a 3x3 matrix")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original array: \n ", A)
A[[0,2],:] = A[[2,0],:]
print("After swap 2 rows in a 3x3 matrix: \n", A)

# calculate mean and standard deviation of an integer array
print("Calculate mean and standard deviation of an integer array")
a = [1,2,3,4,5,6,7,8,9]
mean = np.mean(a)
std = np.std(a)
print("a = ", a)
print("mean = ", mean)
print("std = ", std)

# convert string 'P' and 'NP' to number 0 and 1 respectively
a = [1,2,3,'P',4,5,6,'NP']
print("Convert string 'P' and 'NP' to number 0 and 1 respectively")
b = []
for i in a:
  if i == 'P':
    b.append(0)
  elif i == 'NP':
    b.append(1)
  else:
    b.append(i)
print("a = ", a)
print("b = ", b)
