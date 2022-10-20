def merge(list, start_index, end_index):
    if start_index >= len(list):
        start_index = len(list) - 1
    elif start_index < -len(list):
        start_index = -len(list)
    if end_index >= len(list):
        end_index = len(list) - 1
    elif end_index < -len(list):
        end_index = -len(list)
    list[start_index:end_index + 1] = ["".join(list[start_index:end_index + 1])]
    return list


def divide(list, index, partitions):
    if index >= len(list):
        index = len(list) - 1
    elif index < -len(list):
        index = -len(list)
    split_item = list.pop(index)
    split_list = []
    divider = len(split_item) // partitions
    for i in range(0, len(split_item), divider):
        split_list.append(split_item[i:i + divider])
    for x in split_list:
        list.insert(index, x)
        index += 1
    return list


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
        divide(some_string, int(start_index_or_index), int(end_index_or_partitions))
    command = input()
print(" ".join(some_string))
