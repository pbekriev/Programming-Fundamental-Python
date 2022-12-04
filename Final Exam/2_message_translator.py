import re

number_of_strings = int(input())
pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for _ in range(number_of_strings):
    some_string = input()
    result = re.search(pattern, some_string)
    if result:
        list = [str(ord(x)) for x in result.group(2)]
        print(f"{result.group(1)}: {' '.join(list)}")

    else:
        print("The message is invalid")
