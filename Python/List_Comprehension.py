from math import pi
print([round(pi , i) for i in range(10)])
square = []

for x in range(10):
    square.append(x**2)
print(square)

square2 = list(map(lambda x : x**2, range(0,11)))
print(square2)

square3 = [x **2 for x in range(1,11)] 
print(square3)
print(round(pi , 15))