phonebook = {}
while True:
    command = input()
    if not command.isdigit():
        split_command = command.split('-')
        phonebook[split_command[0]] = split_command[1]
    else:
        for loop in range(int(command)):
            search = input()
            if search in phonebook:
                print(f"{search} -> {phonebook[search]}")
            else:
                print(f"Contact {search} does not exist.")
        break
