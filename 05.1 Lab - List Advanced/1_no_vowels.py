text = input()
list = ['a', 'o', 'u', 'e', 'i']
new_list = [x for x in text if x not in list]
print(''.join(new_list))
