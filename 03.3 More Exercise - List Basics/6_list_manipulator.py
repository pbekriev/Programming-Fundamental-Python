list_of_numbers = input().split()
command = input()
exchange_list = []
while command != "end":
    odd_list = [int(odd) for odd in exchange_list if int(odd) % 2 != 0]
    even_list = [int(even) for even in exchange_list if int(even) % 2 == 0]
    command_list = command.split()
    if "exchange" in command_list:
        if 0 <= int(command_list[1]) < len(list_of_numbers):
            exchange_list = list_of_numbers[int(command_list[1]) + 1:] + list_of_numbers[:int(command_list[1]) + 1]
        else:
            print("Invalid index")
    elif "max" or "min" in command_list:
        if "odd" and "max" in command_list:
            # odd_list = [int(odd) for odd in exchange_list if int(odd) % 2 != 0]
            check_same_odd_index = [index for index, odd_value in enumerate(exchange_list) if
                                    int(odd_value) == sorted(odd_list)[-1]]
            print(check_same_odd_index[-1])
        elif "even" and "max" in command_list:
            even_list = [int(even) for even in exchange_list if even % 2 == 0]
            check_same_even_index = [index for index, even_value in enumerate(exchange_list) if
                                     int(even_value) == sorted(even_list)[-1]]
            print(check_same_even_index[-1])
        elif "odd" and "min" in command_list:
            odd_list = [odd for odd in exchange_list if odd % 2 != 0]
            check_same_odd_index = [index for index, odd_value in enumerate(exchange_list) if
                                    odd_value == sorted(odd_list)[0]]
            print(check_same_odd_index[-1])
        elif "even" and "min" in command_list:
            even_list = [even for even in exchange_list if even % 2 == 0]
            check_same_even_index = [index for index, even_value in enumerate(exchange_list) if
                                     even_value == sorted(even_list)[0]]
            print(check_same_even_index[-1])
    else:
        if "first" and "odd" in command_list:
            odd_list = [odd for odd in exchange_list if odd % 2 != 0]
            print(sorted(odd_list)[:int(command_list[1])])
        elif "first" and "even" in command_list:
            even_list = [even for even in exchange_list if even % 2 == 0]
            print(sorted(even_list)[:int(command_list[1])])
    command = input()
