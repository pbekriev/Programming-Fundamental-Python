# number = input()
#
# for num in range (1, int(number) + 1):
#     digit = str(num)
#
#     def sum_digits(digit):
#         return sum(int(x) for x in digit if x.isdigit())
#
#     if (sum_digits(digit) == 5) or (sum_digits(digit) == 7) or (sum_digits(digit) == 11):
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")

number = int(input())

for current_number in range(1, number + 1):
    digit_sum = 0
    digit_sum += current_number % 10 + int(current_number / 10)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f'{current_number} -> True')
    else:
        print(f'{current_number} -> False')