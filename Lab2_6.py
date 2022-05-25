a=np.arange(0, 45, 5) 
a=a.reshape(3,3) 
for x in np.nditer(a): # n-dimension iterator 
  print(x) 
