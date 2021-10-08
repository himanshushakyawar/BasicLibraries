import numpy as np
a = np.array(np.random.rand(12)*10).reshape(5,2)
print(a)

b = a.astype(int)
print(b)