list_of_number = input().split()
count_of_numbers_to_remove = int(input())
# list_of_number_digit = []
# for digit in list_of_number:
#     list_of_number_digit.append(int(digit))
list_of_number_digit = [int(digit) for digit in list_of_number]  # other way
for _ in range(count_of_numbers_to_remove):
    list_of_number_digit.remove(min(list_of_number_digit))
list_of_strings = [str(simbols) for simbols in list_of_number_digit]
print(", ".join(list_of_strings))
