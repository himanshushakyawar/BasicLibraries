from collections import counter
if __name__ == "__main__":
    
    N  = int(input())
    shoe_list = map(int,input())
    num_cust = int(input())
       
    d = dict(input().split() for _ in range(num_cust))

    print(d)
        
       