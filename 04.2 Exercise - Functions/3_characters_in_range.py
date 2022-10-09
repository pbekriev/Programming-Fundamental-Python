def between_characters(first, second):
    character = []
    for current in range(ord(first)+1, ord(second)):
        character.append(chr(current))
    return character


first_character = input()
second_character = input()
result = between_characters(first_character, second_character)
print(" ".join(result))
