import numpy as np
arr2d = np.array([[1,2,3],[3,2,1]]) #2D array
# arr3d = np.array([[[2,3,4,5],[8,9,6,3]],[[3,6,5,4],[4,5,6,3]]])
# # print(arr3d)
# # print(type(arr))
# # print(arr3d.ndim)
# arrNd = np.array([1,2,3,4], ndmin = 6)
# print(arrNd)
# print(arrNd.ndim)
arr = np.array([1,2,3,4])
print(arr[1] + arr[2])
print("accessing 1 element on 2 dim ", arr2d[1,0])

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[9,6,3]],[[9,5,1],[7,5,300]]])
print(arr3d[2,1,2])