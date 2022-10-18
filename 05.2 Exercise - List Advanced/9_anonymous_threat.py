def merge(list, start_index, end_index):
    list[start_index:end_index + 1] = ["".join(list[start_index:end_index + 1])]
    return list


def divide(list, index, partitions):
    pass


some_string = input().split()
command = input()

while command != "3:1":
    split_command = command.split()
    action = split_command[0]
    start_index_or_index = split_command[1]
    end_index_or_partitions = split_command[2]
    if action == "merge":
        merge(some_string, int(start_index_or_index), int(end_index_or_partitions))
    elif action == "divide":
        pass
    command = input()
print(" ".join(some_string))
