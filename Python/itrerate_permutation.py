from itertools import permutations

if __name__ == "__main__":
    s ,r = map(str, input().split())
    
    
    perm = list(permutations(sorted(s),int(r)))
    for x in perm:
        print(''.join(x))
        

# Sample Input

# HACK 2
# Sample Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# Explanation

# All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.