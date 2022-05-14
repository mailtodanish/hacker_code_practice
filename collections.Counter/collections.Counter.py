# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
from collections import Counter

availbale_shoes_of_size=[]
# print("Number of Shoes :")
number_of_shoes =  int(input())
availbale_shoes_of_size = dict(Counter(list(map(int, input().split()))))

customer_demand =[]
# print("Number of Customer :")
for k in range(int(input())):
    customer_demand.append(input().split())

total = 0
for demand in customer_demand:
    availble = availbale_shoes_of_size.get(int(demand[0]), None)
    if availble:
        total = total + int(demand[1])
        availbale_shoes_of_size[int(demand[0])] = availble - 1
    
    

print(total)