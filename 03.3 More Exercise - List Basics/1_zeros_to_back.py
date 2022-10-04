start_list = input().split(", ")
for number in start_list:
    start_list.append(start_list.pop(start_list.index("0")))
start_list = [int(x) for x in start_list]
print(start_list)