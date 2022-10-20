def increase_decrease(list, value):
    list_for_return = []
    for item in list:
        if item <= value:
            list_for_return.append(item + value)
        elif item > value:
            list_for_return.append(item - value)
    return list_for_return

some_list = list(map(int, input().split()))

removed_index_list = []

while some_list:
    index_for_remove = int(input())
    if len(some_list) == 1:
        removed_index_list.append(some_list.pop(0))
    elif index_for_remove < 0:
        removed_index_list.append(some_list.pop(0))
        some_list.insert(0, some_list[-1])
    elif index_for_remove >= len(some_list):
        removed_index_list.append(some_list.pop(-1))
        some_list.insert(len(some_list), some_list[0])
    else:
        removed_index_list.append(some_list.pop(index_for_remove))
    some_list = increase_decrease(some_list, removed_index_list[-1])

print(sum(removed_index_list))
