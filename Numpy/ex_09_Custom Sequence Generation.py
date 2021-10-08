import numpy as np

a = np.array([x for x in range(0,101,2)])
print(a)

#alternate
b = np.arange(0,100,2, dtype=float).reshape(5,10)
print(b)