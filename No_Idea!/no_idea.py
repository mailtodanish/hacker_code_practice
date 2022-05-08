# 3 2
# 1 5 3
# 3 1
# 5 7
import sys
from collections import Counter
input1 = (sys.stdin.readline()).split()
input2 = (sys.stdin.readline()).split()
input3 = (sys.stdin.readline()).split()
input4 = (sys.stdin.readline()).split()

d = Counter(input2)
happiness = 0
for i in input3:
    happiness = happiness + d[i]

for i in input4:
    happiness = happiness - d[i]

sys.stdout.write(str(happiness))
