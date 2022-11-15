first_char = ord(input())
second_char = ord(input())
string = input()
total_sum = 0
for character in string:
    if first_char < ord(character) < second_char:
        total_sum += ord(character)

print(total_sum)