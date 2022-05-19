import numpy as np 
 
A=np.ones((5,3)) 
B=5*np.ones((5,3)) 
C=np.random.randint(-5,5,(3,5)) 
 
np.multiply(A,B) # elem times elem, not matrix multiplication 
A/B 
A+=B 
A**=B 
np.sqrt(A) 
np.power(A,2) 
np.exp(A) 
 
np.dot(A,B.T) 
 
a= np.array([[-2, 1, 1],[0,2,0],[-4,1,3]]) 
 
print(a.shape) 
b=np.array([4, 5, 6]) 
print(b.T.shape) 
c=np.dot(a,b.T) 
c.shape   
 
np.linalg.det(a) # determinant 
np.linalg.inv(a) # inverse matrix 
eigval, eigvec = np.linalg.eig(a) # a must be square 
     # return eigen values and eigen vectors 
# each col in eigvec is each eigval's corresponding vector 
eigval 
eigvec
