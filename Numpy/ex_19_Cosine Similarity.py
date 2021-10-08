# Cosine similarity is the cosine of the angle between two n-dimensional vectors in an n-dimensional space. 
# It is the dot product of the two vectors divided by the product of the two vectors' lengths (or magnitudes).
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi, 1000)

y = np.cos(x)

plt.plot(x,y)
plt.show()
