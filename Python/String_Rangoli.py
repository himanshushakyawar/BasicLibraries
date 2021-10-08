import string

def print_rang(size):
    alph = string.ascii_lowercase
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = alph[size:x:-1]+alph[x:size]
        print("-".join(line))


if __name__ == "__main__":
    n = int(input())
    print_rang(n)
