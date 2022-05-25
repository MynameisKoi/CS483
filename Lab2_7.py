for x in np.nditer(a, order="C"): # In c seq iteration 
  print(x) 
 
for x in np.nditer(a, order="F"): # In Fortran seq iteration 
  print(x) 
