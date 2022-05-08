# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from itertools import permutations

a = input().split()

ls = []
for c in a[0]:
    if ord(c) >= 65 and ord(c) <= 97:
        ls.append(c)
ls.sort()
ls = list(permutations(ls, int(a[1])))

for t in ls:
    print("".join(t))
