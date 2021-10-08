import numpy as np

arr = np.array([1,2.3,1,5,6], dtype="i")
x = arr.copy() #it doesnt change the copied array at x
arr[2]=122
print(arr)
print(x)


arr1 = np.array([1,2.3,1,5,6], dtype="i")
x= arr1.view()
arr1[1] = 45 #Change in orginal array "arr1" affected the array 'x'

print(arr1)
print(x)

arr2 = np.array([1,2.3,1,5,6], dtype="i")
x = arr2.view()

x[2] = 2000 #change in the View arry as change the orginal array.
print(x)
print(arr2)


#base method

arr2 = np.array([1,2.3,1,5,6], dtype="i")

x = arr2.copy()
y=arr2.view()

print(x.base)
print(y.base)