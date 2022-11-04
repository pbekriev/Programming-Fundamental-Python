number = int(input())
my_dict = {}
for loop in range(number):
    key = input()
    value = input()
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(value)
for word in my_dict.keys():
    print(f"{word} - {', '.join(my_dict[word])}")
