import numpy as np

a= np.array(np.random.randint(1,50,4).reshape(2,2))
b= np.array(np.random.randint(1,50,4).reshape(2,2))

print(a)
print(b)

# c = np.concatenate((a,b), axis=0)
c = np.hstack((a,b))
print(c)

d= np.vstack((a,b))
print(d)

