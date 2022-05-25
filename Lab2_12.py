import numpy as np 
from sklearn.linear_model import LinearRegression 
 
x = np.array([1,3,5,7,9,11,13,15,17,19]).reshape((-1, 1)) 
# reshape((-1, 1)) : '-1' means unknown number of row; '1' means one column 
y = np.array([3,3,7,7,11,11,15,15,19,19]) 
 
model = LinearRegression().fit(x, y) 
 
print('intercept:', model.intercept_) 
print('slope:', model.coef_) 
y_pred = model.predict(x) 
print('predicted response:', y_pred, sep='\n') 
new_y = model.predict([[20]]) 
print('predicted response if x=20:', new_y , sep='\n') 
 
