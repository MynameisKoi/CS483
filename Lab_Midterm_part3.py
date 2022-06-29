import numpy as np
import pandas as pd

# change 1d array from 0 to 8 to 3x3 matrix
print("Change 1d array from 0 to 8 to 3x3 matrix")
a = [0,1,2,3,4,5,6,7,8]
b = np.array(a).reshape(3,3)
print("a = ", a)
print("b = ", b)

# calculate the Euclidean distance from two 1d arrays
print("Calculate the Euclidean distance from two 1d arrays")
a = np.array([1,2,3])
b = np.array([4,5,6])
print("a = ", a)
print("b = ", b)
print("Euclidean distance = ", np.linalg.norm(a-b))

# only import odd number rows from a csv file
print("Only import odd number rows from a csv file")
from google.colab import drive
drive.mount('/content/drive')         
data_path = "/content/drive/My Drive/Colab Notebooks/newcsv4.csv"
df = pd.read_csv(data_path)
df = df[df.index % 2 == 1]
print(df)

# substitute all elements in diagonals to 0 in a 5x5 matrix
print("Substitute all elements in diagonals to 0 in a 5x5 matrix")
A = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print("Original array: \n ", A)
for i in range(len(A)):
    A[i][i] = 0
print("After substitute all elements in diagonals to 0 in a 5x5 matrix: \n", A)

# separate a dataframe 80% to trainingset and 20% to testset
print("Separate a dataframe 80% to trainingset and 20% to testset")
df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/newcsv4.csv")
df_train = df.sample(frac=0.8, random_state=1)
df_test = df.drop(df_train.index)
print("df_train = \n", df_train)
print("df_test = \n", df_test)
