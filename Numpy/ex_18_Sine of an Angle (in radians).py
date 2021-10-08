import numpy as np
import matplotlib.pylab as plt

x = np.linspace(-3.14,3.14, 1000)
# a = x*(180/3.14)
# print(a)
# print(x)

y = np.sin(x)

plt.plot(x,y)
plt.xlabel("Degree in radians")
plt.ylabel("Sin(x)")
plt.axis("tight")
plt.show()
