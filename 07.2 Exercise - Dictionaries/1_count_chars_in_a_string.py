some_string = input().split()
one_word = "".join(some_string)
my_dict = {}

for char in one_word:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")
