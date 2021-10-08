# https://www.hackerrank.com/challenges/camelcase/problem

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    s_set = set(s)
    print(s_set)
    count = [i for i in s_set if i.isupper()]
    print(count)
    return (len(count)+1)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
