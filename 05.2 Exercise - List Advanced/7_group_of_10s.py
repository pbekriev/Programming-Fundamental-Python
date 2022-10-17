def filtering(list_for_filter, boundary_value):
    list_for_return = list_for_filter.copy()
    filtered_list = []
    for number in list_for_filter:
        if number <= boundary_value:
            filtered_list.append(number)
            list_for_return.remove(number)
    print(f"Group of {boundary_value}'s: {filtered_list}")
    boundary_value += 10
    return list_for_return, boundary_value


list_of_numbers = list(map(int, input().split(", ")))
boundary = 10

while list_of_numbers:
    if boundary == 10:
        list_of_numbers, boundary = filtering(list_of_numbers, boundary)
    elif boundary == 20:
        list_of_numbers, boundary = filtering(list_of_numbers, boundary)
    elif boundary == 30:
        list_of_numbers, boundary = filtering(list_of_numbers, boundary)
    elif boundary == 40:
        list_of_numbers, boundary = filtering(list_of_numbers, boundary)
    else:
        list_of_numbers, boundary = filtering(list_of_numbers, boundary)
