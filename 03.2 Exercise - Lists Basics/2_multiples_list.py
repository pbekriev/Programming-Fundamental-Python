factor = int(input())
count = int(input())

list_of_number = []
# current_number = 0
#
# for loop in range(count):
#     current_number += factor
#     list_of_number.append(current_number)

for number in range(1,count + 1):
    list_of_number.append(number * factor)

print(list_of_number)
