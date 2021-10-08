import numpy as np

a = np.array(np.random.randint(1,100,60))
print(a) #1-D array
print(a.shape) #1-D array

# Converting 1-D array to 3-D Array

b= a.reshape(3,2,10)
print(b)
print(b.base)
print(b.shape)