def positive_num(some_num):
    return [num for num in some_num if int(num) >= 0]


def negative_num(some_num):
    return [num for num in some_num if int(num) < 0]


def even_num(some_num):
    return [num for num in some_num if int(num) % 2 == 0]


def odd_num(some_num):
    return [num for num in some_num if int(num) % 2 != 0 ]


list_of_number = input().split(', ')

print(f"Positive: {', '.join(positive_num(list_of_number))}")
print(f"Negative: {', '.join(negative_num(list_of_number))}")
print(f"Even: {', '.join(even_num(list_of_number))}")
print(f"Odd: {', '.join(odd_num(list_of_number))}")