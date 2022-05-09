# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen

from itertools import combinations_with_replacement

a = input().split()

ls = []
for c in a[0]:
    if ord(c) >= 65 and ord(c) <= 97:
        ls.append(c)
ls.sort()
k=int(a[1])
new_list = list(combinations_with_replacement(ls, k))

for t in new_list:
    print("".join(t))
