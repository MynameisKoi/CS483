import numpy as np 
 
x=np.linspace(-10,10,201) 
x1=np.arange(-10.0, 10.0, 0.1) 
sine=np.sin(x) 
 
import matplotlib.pyplot as plt 
 
plt.plot(x,sine) 
plt.show() 
 
quad1=x**2 + 2.0*x +5.0 
plt.plot(x,quad1) 
plt.show() 
 
def norm_func(x,mean,var): 
  return 1.0/(var*(2*np.pi)**0.5) * np.exp(-1/2*((x-mean)/var)**2) 
 
x=np.arange(-5,5.01,0.05) 
pdf1=norm_func(x,0,0.2**0.5) 
pdf2=norm_func(x,0,1.0**0.5) 
pdf3=norm_func(x,0,5.0**0.5) 
pdf4=norm_func(x,-2.0,0.5**0.5) 
 
plt.plot(x,pdf1,color='blue', label="mean={} var^2={}".format(0,0.2)) 
plt.plot(x,pdf2,color='red', label="mean={} var^2={}".format(0,1.0)) 
plt.plot(x,pdf3,color='yellow', label="mean={} var^2={}".format(0,5.0)) 
plt.plot(x,pdf4,color='green', label="mean={} var^2={}".format(-2.0,0.5)) 
plt.legend() 
plt.show()
