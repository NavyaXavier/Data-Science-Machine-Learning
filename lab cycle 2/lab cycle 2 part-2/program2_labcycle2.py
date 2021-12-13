import numpy as np 
arr1 =np.array([[1, 2, 3],[3,2,4],[2,2,1]])
print(arr1)
print(pow(arr1, 3))
print(np.multiply(arr1,(arr1*arr1)))
print(arr1*arr1*arr1)
print(arr1**3)
b = np.identity(3, dtype = int)
print("Identity matrix:\n", b)
