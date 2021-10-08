import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]])
arr5d = np.array([[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]]], ndmin = 5)
print(arr5d.reshape(-1))
# print(arr1.shape)
# print(arr2.shape)
# print(arr1.reshape(9,1).shape)

# print(arr5d.shape)

# arrMul = np.array([i for i in range(0,24)])
# print(arrMul.reshape(4,3,2,1))
# # print(arrMul.reshape(10,1).shape)

# arrX = arrMul.reshape(12,2) #It Create a View So, if their is achange in the arrX it will reflect in the arrMul
# print(arrX)
# arrX[2,1] = 10 
# print(arrX)
# print(arrX.base)
# print(arrMul) 


