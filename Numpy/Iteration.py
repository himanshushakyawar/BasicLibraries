import numpy as np
arr1d = np.array([2,3,45,7.6,54,64,6,4])

# for x in arr1d:
#     print(x)

arr2d = np.array([[[2,3,45,7.6,54,64,6,4],[12,13,415,17.6,154,614,61,14]]])
# print(arr2d.shape)

# for x in arr2d:
#     for y in x:
#         for z in y:
#             print(z)
#         # for z in y:
#         #     print(z)
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for n in np.nditer(arr3d[:,::2]):
#     print(n)

# print(arr3d[0,0,1])
# for n in np.nditer(arr3d, flags=['buffered'],op_dtypes='U'): 
#     print(n)   


for index, value in np.ndenumerate(arr3d):
    print(index, value)