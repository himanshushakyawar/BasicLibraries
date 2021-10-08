import numpy as np
arr1 = np.array([[1,2,3],[3,4,5]], dtype="i")
arr2 = np.array([[4,5,6],[6,4,2]], dtype='i')

# newarr = np.concatenate((arr1,arr2), axis=1)
arr3 = np.array([1,2,3], dtype="i")
arr4 = np.array([3,4,5])
# newarr1 = np.concatenate((arr3,arr4), axis = 0)
# print(newarr1)
# newarr = np.stack((arr3,arr4), axis=1)
# print(newarr)
# newarr3 = np.column_stack((arr3,arr4))
# print(newarr3)

# newarr3 = np.hstack((arr3,arr4))
# print(newarr3)

# newarr3 = np.vstack((arr3,arr4))
# print(newarr3)

newarr3 = np.dstack((arr3,arr4))
print(arr3)
print(arr4)
print(newarr3)
