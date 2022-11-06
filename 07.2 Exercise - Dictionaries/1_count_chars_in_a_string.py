some_string = input().split()
my_dict = {}

for item in some_string:
    for char in item:
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] += 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")
