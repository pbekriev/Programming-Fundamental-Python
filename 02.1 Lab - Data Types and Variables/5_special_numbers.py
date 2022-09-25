number = int(input())
sum_of_digits = 0

for loop_of_number in range(1, number + 1):
    for digit in str(loop_of_number):
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{loop_of_number} -> True")
    else:
        print(f"{loop_of_number} -> False")
    sum_of_digits = 0