def find_negativ_or_positive(num_1, num_2, num_3):
    negativ_count = 0
    list_of_num = [num_1, num_2, num_3]
    for number in list_of_num:
        if number == 0:
            return "zero"
        elif number < 0:
            negativ_count += 1
    if negativ_count == 2 or negativ_count == 0:
        return "positive"
    else:
        return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(find_negativ_or_positive(first_number, second_number, third_number))
