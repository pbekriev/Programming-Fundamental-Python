key = input().split()
decrypt = ""
while True:
    command = input()
    age_start = 0
    age_end = 0
    if command == "find":
        break
    key_index = 0
    for character in command:
        if key_index == len(key):
            key_index = 0
        decrypt += chr(ord(character) - int(key[key_index]))
        key_index += 1
    for index in range(len(decrypt)):
        if decrypt[index] == "<":
            age_start = index + 1
        if decrypt[index] == ">":
            age_end = index

    print(f"Found {decrypt.split('&')[1]} at {decrypt[age_start:age_end]}")
    decrypt = ""