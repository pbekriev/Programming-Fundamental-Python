list_of_number = input().split()
opposite_numbers = []

for number in list_of_number:
    current_number = -int(number)
    opposite_numbers.append(current_number)

print(opposite_numbers)
