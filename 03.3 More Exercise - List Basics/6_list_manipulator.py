list_of_numbers = input().split()
command = input().split()
exchange_list = list_of_numbers
while "end" not in command:
    odd_list = [int(odd) for odd in exchange_list if int(odd) % 2 != 0]
    even_list = [int(even) for even in exchange_list if int(even) % 2 == 0]
    if "exchange" in command:
        if 0 <= int(command[1]) < len(list_of_numbers):
            exchange_list = list_of_numbers[int(command[1]) + 1:] + list_of_numbers[:int(command[1]) + 1]
        else:
            print("Invalid index")
    elif "max" in command:
        if ("odd" in command) and odd_list:
            check_same_odd_index = [index for index, odd_value in enumerate(exchange_list) if
                                    int(odd_value) == sorted(odd_list)[-1]]
            print(check_same_odd_index[-1])
        elif ("even" in command) and even_list:
            check_same_even_index = [index for index, even_value in enumerate(exchange_list) if
                                     int(even_value) == sorted(even_list)[-1]]
            print(check_same_even_index[-1])
        else:
            print("No matches")
    elif "min" in command:
        if ("odd" in command) and odd_list:
            check_same_odd_index = [index for index, odd_value in enumerate(exchange_list) if
                                    int(odd_value) == sorted(odd_list)[0]]
            print(check_same_odd_index[-1])
        elif ("even" in command) and even_list:
            check_same_even_index = [index for index, even_value in enumerate(exchange_list) if
                                     int(even_value) == sorted(even_list)[0]]
            print(check_same_even_index[-1])
        else:
            print("No matches")
    else:
        if int(command[1]) <= len(exchange_list):
            if "first" in command:
                if "odd" in command:
                    print(odd_list[:int(command[1])])
                elif "even" in command:
                    print(even_list[:int(command[1])])
            else:
                if "odd" in command:
                    print(odd_list[-int(command[1]):])
                elif "even" in command:
                    print(even_list[-int(command[1]):])
        else:
            print("Invalid count")
    list_of_numbers = exchange_list
    command = input().split()
exchange_list = [int(x) for x in exchange_list]
print(exchange_list)
