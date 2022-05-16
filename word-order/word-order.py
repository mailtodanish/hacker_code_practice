'''
# TODO: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# inputs :
# 4
# bcdef
# abcdefg
# bcde
# bcdef

'''


from collections import Counter

n = int(input())
lst_of_words = []
for i in range(n):
    lst_of_words.append(input())

count = dict(Counter(lst_of_words))
print(len(count))
values = list(map(str, list(count.values())))
print(" ".join(values))
