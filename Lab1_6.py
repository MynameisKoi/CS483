import numpy as np 
 
x=np.linspace(-4,4,9) 
y=np.linspace(-5,5,11) 
 
xx,yy=np.meshgrid(x,y, sparse=True)  
# sparse: change xx/yy format from multi-dim to 1 dim, but it is still mult-dim 
xx 
yy 
xx.shape 
yy.shape 
 
ell=xx**2 + yy**2    # Verify above explanation 
 
xm,ym=np.mgrid[-11:12:2.5, -11:12:2.5] # similar as meshgrid, but diff.  
 
xm,ym=np.mgrid[-11:12:5j, -11:12:5j] # 5j - 5 points within the range, not a 
step 
xm.shape 
ym.shape 
 
xm,ym=np.ogrid[-11:12:5j, -11:12:5j] # similar as mgrid 
 
xg, yg=np.broadcast_arrays(xm,ym)   
# make x matrix format follow y matrix format
