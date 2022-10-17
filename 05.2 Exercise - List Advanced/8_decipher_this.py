def decipher(word_for_decipher):
    digits = ""
    string = ""
    for digit in word_for_decipher:
        if digit.isdigit():
            digits += digit
        else:
            string += digit
    if len(string) > 1:
        string_list = [x for x in string]
        string_list[0], string_list[-1] = string_list[-1], string_list[0]
        string = ''.join(string_list)
    return chr(int(digits)) + string


secret_message = input().split()
decipher_message = []
for secret_word in secret_message:
    decipher_message.append(decipher(secret_word))
print(" ".join(decipher_message))
