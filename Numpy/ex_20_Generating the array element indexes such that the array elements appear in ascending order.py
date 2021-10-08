import numpy as np

import matplotlib.pyplot as plt


a = np.random.randint(1,20, 10)
print(a)

b = np.argmax(a)  ##Return index of maxValue
print(b)
c=np.argsort(a)
print(c)
d = np.sort(a)
print(d)