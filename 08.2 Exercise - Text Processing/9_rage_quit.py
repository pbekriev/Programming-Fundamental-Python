some_string = input().upper()
output_string = ""
last_index = 0
repeatedly_n = 0
for index in range(len(some_string)):
    if some_string[index].isdigit():
        if index + 1 < len(some_string) and some_string[index + 1].isdigit():
            repeatedly_n = int(some_string[index] + some_string[index + 1])
            output_string += some_string[last_index:index] * repeatedly_n
            last_index = index + 2
        else:
            repeatedly_n = int(some_string[index])
            output_string += some_string[last_index:index] * repeatedly_n
            last_index = index + 1
print(f"Unique symbols used: {len(set(output_string))}")
print(output_string)
