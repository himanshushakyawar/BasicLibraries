import numpy as np

arr = np.array([1,2,4,4,5,6,7,8,9,4])
# x = np.where(arr ==4)
# print(x)

# y=np.where(arr%2==1)
# print(y)

#Search Sort

arr = np.array([2, 7, 3, 9,1,56])

c = np.searchsorted(arr,[6,5,0])

print(c)