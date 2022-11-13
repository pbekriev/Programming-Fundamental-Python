digit = int(input())
digit_for_count = int(input())
count = 0
list_of_numbers = []
while digit > 0:
    rest = digit % 2
    digit = digit // 2
    list_of_numbers.append(str(rest))
    if rest == digit_for_count:
        count += 1
print("".join(list_of_numbers[::-1]))
print(count)