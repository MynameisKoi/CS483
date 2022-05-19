import numpy as np

np.eye(4)  # get eye matrix
# result: array([[1., 0., 0., 0.],
#                [0., 1., 0., 0.],
#                [0., 0., 1., 0.],
#                [0., 0., 0., 1.]])

np.identity(3)  # like eye function
# result: array([[1., 0., 0.],
#                [0., 1., 0.],
#                [0., 0., 1.]])

z = np.zeros((3,4), dtype=int)
z = np.ones((3,4), dtype=np.float64)

z=np.random.random(())
z=np.random.uniform(-3, 5, (5,6))
## get 5x6 matrix with random # from -3 to 5 for each elem 
