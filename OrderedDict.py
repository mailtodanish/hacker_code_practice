# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
from collections import OrderedDict
ordered_dictionary = OrderedDict()
n = int(input())
for i in range(n):
    item = input().split(" ")
    price = int(item.pop())
    name = " ".join(item)
    ordered_dictionary[name] = ordered_dictionary.get(name, 0) + int(price)
for key, value in ordered_dictionary.items():
    print(key, value)
