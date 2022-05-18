from collections import defaultdict
d = defaultdict(list)
i = list(map(int, input().split()))
for x in range(i[0]):
    d['a'].append(input())
for x in range(i[1]):
    d['b'].append(input())


for item in d['b']:
    res = [str(idx+1) for idx, val in enumerate(d['a']) if val ==item ]
    if len(res) < 1:
        res.append("-1")
    print(" ".join(res))