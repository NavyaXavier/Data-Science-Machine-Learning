import numpy as np 

a1= np.array([[1,2,3],[3,4,5]])
print(a1)
print("Number of rows and columns of the said matrix")
print(a1.shape)
print("dimension")
print(a1.ndim)
print("reshape tha array to 3x2")
newarr = a1.reshape(3,2)
print(newarr)
