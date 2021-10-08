import numpy as np

a = np.array(np.random.randint(0,2,12)).reshape(4,3)
print(a)

b = a.astype("bool")
print(b)
