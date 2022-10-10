def smallest_number(number):
    return min(number)

first_num = int(input())
second_num = int(input())
third_num = int(input())
all_numbers = [first_num, second_num, third_num]
min_number = smallest_number(all_numbers)
print(min_number)