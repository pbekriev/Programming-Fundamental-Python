some_string = input()
command = input()
while command != "End":
    split_command = command.split()
    current_command = split_command[0]
    if current_command == "Translate":
        char, replacement = split_command[1], split_command[2]
        some_string = some_string.replace(char, replacement)
        print(some_string)

    elif current_command == "Includes":
        substring = split_command[1]
        if substring in some_string:
            print("True")
        else:
            print("False")

    elif current_command == "Start":
        substring = split_command[1]
        if substring == some_string[:len(substring)]:
            print("True")
        else:
            print("False")

    elif current_command == "Lowercase":
        some_string = some_string.lower()
        print(some_string)

    elif current_command == "FindIndex":
        char = split_command[1]
        print(some_string.rfind(char))

    elif current_command == "Remove":
        start_index, count = int(split_command[1]), int(split_command[2])
        some_string = some_string[:start_index]+some_string[start_index + count:]
        print(some_string)

    command = input()
