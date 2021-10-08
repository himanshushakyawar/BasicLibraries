if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    set1 = set(arr)
    newarr = list(set1)
    if len(newarr) <2 :
        print(newarr[-1])
    else:
        print(newarr[-2])
    