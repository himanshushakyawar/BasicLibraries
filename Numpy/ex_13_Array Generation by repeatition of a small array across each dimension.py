import numpy as np

a = np.array([[2,3,6],
            [9,6,4]])

print(a)

b = np.tile(a,(2,2))

# a = np.array([0, 1, 2])
# np.tile(a, 2)
# array([0, 1, 2, 0, 1, 2])
# np.tile(a, (2, 2))
# array([[0, 1, 2, 0, 1, 2],
#        [0, 1, 2, 0, 1, 2]])
# np.tile(a, (2, 1, 2))
# array([[[0, 1, 2, 0, 1, 2]],
#        [[0, 1, 2, 0, 1, 2]]])

print(b)