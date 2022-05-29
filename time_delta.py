# Fri 11 Feb 2078 00:05:21 +0400
# Mon 29 Dec 2064 03:33:48 -1100
from datetime import datetime
pattern =  '%a %d %b %Y %H:%M:%S %z'
i = int(input())
for j in range(i) :
    t1 = datetime.strptime(input() , pattern)
    t2 = datetime.strptime(input(), pattern)
    print(abs(int(t1.timestamp()-t2.timestamp())))