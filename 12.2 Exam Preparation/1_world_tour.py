stops = input()
command = input()

while command != "Travel":

    split_command = command.split(":")
    current_command = split_command[0]

    if current_command == "Add Stop":
        index, string = int(split_command[1]), split_command[2]
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif current_command == "Remove Stop":
        start_index, end_index = int(split_command[1]), int(split_command[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif current_command == "Switch":
        old_string, new_string = split_command[1], split_command[2]
        stops = stops.replace(old_string, new_string)

    print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")
