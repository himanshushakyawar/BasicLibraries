
if __name__ == '__main__' :
    # n = int(input("Enter the Print integer n in range (1,150): "))

    print(*range(1, int(input())+1), sep='') ## here * mean its taking a list as a argument and argument is range(1, int(input())+1)
    list = range(1, int(input())+1)
    print(list)
