if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    def Cart_prod(x,y):
        
        for i in range(0, len(x)):
            for j in range(0,len(y)):
                elements = tuple((x[i],y[j]))
                print(elements, end=" ")
    
    
                
    Cart_prod(A,B)
    print("\n")
#Alternate Method
from itertools import product

obj = product(A,B)
print(*obj)