from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())

number_of_course = ceil(number_of_people / elevator_capacity)
print(number_of_course)