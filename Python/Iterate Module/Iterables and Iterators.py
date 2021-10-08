# https://www.hackerrank.com/challenges/iterables-and-iterators/problem


from itertools import combinations

if __name__ == "__main__":
    N , ele, k = input(), input().split(), int(input())
    comb = combinations(ele,k)
    fav=0
    total = 0

    
    for i in  list(comb):
        st = "".join(i)
        total+=1
        if st.find('a') !=-1:
            fav+=1
    print("{0:.3f}".format((fav/total)))
    