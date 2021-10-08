if __name__ == "__main__":
    M = int(input())
    set_M = set([map(int,input())])
    
    N = int(input())
    set_N = set([map(int,input())])
    
    item = []
    item.append(set_M.difference(set_N))
    item.append(set_N.difference(set_M))
    
    item = item.sort()
    print(item)
    for x in item:
        print(x)
    
    
    