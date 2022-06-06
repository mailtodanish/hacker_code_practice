# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.

from collections import namedtuple
total_number_of_student = int(input())
marks = namedtuple('marks', input())
students = [marks(*input().split()) for i in range(total_number_of_student)]
print(round(sum([float(x.MARKS) for x in students])/total_number_of_student,2))
