from collections import defaultdict
d = defaultdict(list)
d['python'].append('Awesome')
d['something-else'].append("not relevant")
d['python'].append('Language')
for i in d.items():
    print(i)
