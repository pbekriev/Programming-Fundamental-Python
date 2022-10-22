def merge(list, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(list):
        end_index = len(list) - 1
    if start_index != end_index:
        list[start_index:end_index + 1] = ["".join(list[start_index:end_index + 1])]
    return list


def divide(list, index, partitions):
    if index >= len(list):
        index = len(list) - 1
    elif index < 0:
        index = 0
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

# Other way

# strings_input = input().split()
# result = []
# instructions = input()
# while not instructions == "3:1":
#     instructions = instructions.split()
#     command = instructions[0]
#     if command == 'merge':
#         start = int(instructions[1])
#         end = int(instructions[2])
#         if start < 0:
#             start = 0
#         if end > len(strings_input) - 1:
#             end = len(strings_input) - 1
#         for index, string in enumerate(strings_input):
#             if index in range(start + 1, end + 1):
#                 strings_input[start] += strings_input[index]
#         for index in range(end, start, - 1):
#             strings_input.pop(index)
#     elif command == 'divide':
#         index = int(instructions[1])
#         partitions = int(instructions[2])
#         if partitions > len(strings_input[index]):
#             step = 1
#         else:
#             step = len(strings_input[index]) // partitions
#         divide_part = strings_input.pop(index)
#         start = 0
#         for parts in range(partitions):
#             if parts == partitions - 1:
#                 strings_input.insert(index, divide_part[start::])
#                 break
#             else:
#                 strings_input.insert(index, divide_part[start: start + step:])
#             start += step
#             index += 1
#     instructions = input()
# print(' '.join(strings_input))