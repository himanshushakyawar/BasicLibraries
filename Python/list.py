squares = []
x = 12
# for x in range(0,10):
#     squares.append(x**2)

# print(squares)
# print(x)

##Using Lamda Function

squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)

squares2 = list(x**2 for x in range(20))
print(squares2)

# listcomp = [(x,y) for x in [1,2,3] for y in [1,4,5] if x!=y]
# print(listcomp)

sq4 = [x*2 for x in squares2]
print(sq4)

sq4pos = [x for x in squares2 if x<100]
print(sq4pos)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fd= [weapon.strip() for weapon in freshfruit]

print(fd)

vec = [[1,2,3], [4,5,6], [7,8,9]]
vecFlatten =[num for x in vec for num in x]
print(vecFlatten)

from math import pi
pi = list(str(round(pi + i ,i)) for i in range(10))
print(pi)