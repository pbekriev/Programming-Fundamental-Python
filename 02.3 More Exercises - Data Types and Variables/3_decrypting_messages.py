key = int(input())
number_of_lines = int(input())
decrypted_word = ""

for loop in range (number_of_lines):
    letter_for_decrypting = input()
    decrypted_number = ord(letter_for_decrypting) + key
    decrypted_word += chr(decrypted_number)
print(decrypted_word)