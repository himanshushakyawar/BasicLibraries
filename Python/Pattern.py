# def Cap(name):
#     cap_First = name[0].capitalize()
#     cap_Last = name[1].capitalize()
#     return str(cap_First+" "+cap_Last)




import math
import os
import random
import re
import sys
# if __name__== '__main__' :
#     raw_name = list(map(str,input().split()))
#     ret = Cap(raw_name)
#     print(ret)


def solve(s):
    name = list(map(str,s))
    cap_First = name[0].capitalize()
    cap_Last = name[1].capitalize()
    return str(cap_First+" "+cap_Last)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
