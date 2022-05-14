import math
AB = int(input())
BC = int(input())
theta = math.atan(AB / BC)
degrees = round(theta * 180 / math.pi)
print(degrees,chr(176),sep='')