def even_and_odd_num(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for number in number_str:
        if int(number) % 2 == 0:
            sum_of_even_digits += int(number)
        else:
            sum_of_odd_digits += int(number)
    return sum_of_odd_digits, sum_of_even_digits


number_str = input()
sum_of_odd_digits, sum_of_even_digits = even_and_odd_num(number_str)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
