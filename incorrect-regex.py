import re
n = int(input())

for i in range(n):
    try:
        k = input()
        re.compile(k)
        print(True)
    except re.error:
        print(False)