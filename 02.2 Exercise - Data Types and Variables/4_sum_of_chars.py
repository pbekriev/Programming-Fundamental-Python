number_of_characters = int(input())
total_sum = 0

for character in range (number_of_characters):
    currrent_character = input()
    total_sum += ord(currrent_character)
print(f"The sum equals: {total_sum}")