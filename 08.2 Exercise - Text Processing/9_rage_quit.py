some_string = input()
unique_chart = ""
output_string = ""
last_index = 0
for index in range(len(some_string)):
    if some_string[index] not in unique_chart and not some_string[index].isdigit():
        unique_chart += some_string[index].upper()
    else:
        output_string += some_string[last_index:index].upper() * int(some_string[index])
        last_index = index + 1
print(f"Unique symbols used: {len(set(unique_chart))}")
print(output_string)