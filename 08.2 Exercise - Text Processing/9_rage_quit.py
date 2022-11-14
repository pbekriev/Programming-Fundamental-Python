some_string = input().upper()
unique_chart = ""
output_string = ""
last_index = 0
for index in range(len(some_string)):
    if not some_string[index].isdigit():
        if some_string[index] not in unique_chart:
            unique_chart += some_string[index]
    else:
        output_string += some_string[last_index:index] * int(some_string[index])
        last_index = index + 1
print(f"Unique symbols used: {len(unique_chart)}")
print(output_string)