# https://www.hackerrank.com/challenges/itertools-combinations/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

from itertools import combinations

a = input().split()

ls = []
for c in a[0]:
    if ord(c) >= 65 and ord(c) <= 97:
        ls.append(c)
ls.sort()
for k in range(1,int(a[1])+1):
    new_list = list(combinations(ls, k))

    for t in new_list:
        print("".join(t))
