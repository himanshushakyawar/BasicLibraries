import numpy as np

a = np.random.randint(1,10,size=(6,4))
b = np.random.normal(5,1,size=(4,7))
print(a)
print(b)

c = a@b       #@ for matri multiplication

print(c)