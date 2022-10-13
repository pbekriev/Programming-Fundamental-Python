number = int(input())
wagon = [0] * number
while True:
    command = input()
    if command == 'End':
        break
    split_command = command.split(" ")
    if split_command[0] == 'add':
        wagon[-1] += int(split_command[1])
    elif split_command[0] == 'insert':
        wagon[int(split_command[1])] += int(split_command[2])
    elif split_command[0] == 'leave':
        wagon[int(split_command[1])] -= int(split_command[2])
print(wagon)
