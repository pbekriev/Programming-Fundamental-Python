number = int(input())
pure_or_not = True
for loop in range (number):
    strings = input()
    if "," in strings or \
        "." in  strings or \
        "_" in strings:
        print(f"{strings} is not pure!")
    else:
        print(f"{strings} is pure.")