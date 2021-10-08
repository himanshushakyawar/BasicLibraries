import numpy as np

a = np.full(shape=(5,2), fill_value=10)
b = np.arange(10, 20)
c= np.full_like(b , .1, dtype=float)
print(a)
print(b)
print(c)

# Alternative

g = np.ones(shape=(5,2), dtype=int)
print(g)

h=g*10
print(h)