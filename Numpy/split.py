import numpy as np
from numpy.core.defchararray import split
from numpy.lib.shape_base import array_split


arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([10,20,30,40,50,60,70,80,90,10])
newarr = array_split(arr,3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])


# spliting 2d array

# arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# # print(arr3)?
# newarr = np.array_split(arr3,4)
# print(newarr)
# newarr = np.array_split(arr3,4 ,axis=1)
# print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

marr = np.array_split(arr,4, axis=1)
# print(marr[0])

marr1=np.hsplit(arr,3)
print(marr1)
