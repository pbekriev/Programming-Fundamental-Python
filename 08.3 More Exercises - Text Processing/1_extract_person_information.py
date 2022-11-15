numbers = int(input())
for _ in range(numbers):
    string = input()
    name_start_index = 0
    name_end_index = 0
    age_start_index = 0
    age_end_index = 0

    for index in range(len(string)):
        if string[index] == "@":
            name_start_index = index + 1
        if string[index] == "|":
            name_end_index = index
        if string[index] == "#":
            age_start_index = index + 1
        if string[index] == "*":
            age_end_index = index

    print(f"{string[name_start_index:name_end_index]} is {string[age_start_index:age_end_index]} years old.")