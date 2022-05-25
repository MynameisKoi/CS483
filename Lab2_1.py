import numpy as np 
 
a = np.random.randint(0,10,(5,5)) 
a.max()  # max in all elem in matrix 
a.min()  
a.max(axis=0)  # axis=0 is for each col 
a.max(axis=1)  # axis=1 is for each row 
 
print(a.flatten()) # flatten matrix 
a.argmax()  # flatten matrix first and return max value's index  
a.argmin() 
 
a.argmax(axis=0) # max value's index in each column 
a.argmax(axis=1) # max value's index in each row 
 
a.mean()  # mean from all elem matrix 
a.sum()  # sum of all elem in matrix 
 
a.mean(axis=0) # mean in each column 
a.mean(axis=1) # mean in each row 
a.std()    # standard deviation = sqrt(variance) 
a.std(axis=0)  # standard deviation in each col 
a.var()   # variance  
a.var(axis=0)   # variance in each col  
 
a.cumsum()  # array of cumulative sum  
   # e.g.  
 
# a.cumsum() -> array([1,(1+2),(1+2+3),10,15,21]) 
       
 
a.cumprod()  # array of cumulative product 
   # e.g.  
   
# a.cumprod() -> array([1,(1*2),(1*2*3),10,15,21]) 
      
 
np.sort(a)  # sort matrix row by row 
np.argsort(a)  # return index matrix after sorting row by row 
 
A = np.array([1,2,3]) 
B = np.array([4,5,6]) 
np.average(A, weights=B) # B is matrix 
    # A=[1,2,3]; B=[4,5,6] 
# np.average(A, weight=B) => 1*(4/(4+5+6)) + 2*(5/(4+5+6)) + 3*(6/(4+5+6)) 
 
mult = A*B 
 
np.average(A)  # =np.mean(A) 
 
a=np.array([[1,2],[3,4]]) 
b=np.array([[11,12],[13,14]]) 
np.vdot(a,b)  # e.g. 
    
# np.vdot(a, b)  # 1*11 + 2*12 + 3*13 + 4*14 
 
a=np.array([1,2,3,6,7]) 
np.median(a) 
# median value for 1,2,3,6,7 -> median=3 
# median value for 1,2,6,7   -> (2+6)/2 = 4.0 
 
a=np.array([1,0,0,2,3]) 
a.nonzero()  # a=[1,0,0,2,3]; a.nonzero()=[0, 3, 4] return nonzero elem 
index 
 
np.inner(A,B)   # = A*B.T 
np.dot(A,B)  # = A*B 
 
np.outer(A,B)   # = A.T*B 
A=np.array([[1,2],[3,4]]) 
np.transpose(A)   
 
A.trace()  # sum of all elements in quare-matrix A's diagonal 
A=np.array([3,1,3,4]) 
np.diff(A)  # if A=[3,1,3,4], then np.diff(A) = [(1-3),(3-1),(4-1)]
