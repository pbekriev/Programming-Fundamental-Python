first_string = input()
second_string = input()
last_string = first_string
for character_index in range (len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string


# string = "I am living in Sofia"
# print(string[0:10+1:1])
# print(string[:11])
# print(string[::-1])