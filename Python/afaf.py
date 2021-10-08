def solve(s):
    words = s.split(" ")
    print(words, type(words))
    cap_word = [w.capitalize() for w in words]
    print(cap_word)
    return " ".join(cap_word)
        




d = input()

res = solve(d)
print(res)
