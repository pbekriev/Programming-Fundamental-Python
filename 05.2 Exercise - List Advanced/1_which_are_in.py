first_list = input().split(', ')
second_list = input().split(', ')
final_list = []
for first_list_word in first_list:
    for second_list_word in second_list:
        if first_list_word in second_list_word:
            final_list.append(first_list_word)
            break
print(final_list)