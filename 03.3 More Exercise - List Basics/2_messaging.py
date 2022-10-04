sequence_of_numbers = input().split()
string = input()
string_list = [w for w in string]
text_out = []
for numbers in sequence_of_numbers:
    word_index = sum(int(x) for x in numbers)
    if word_index < len(string):
        text_out += string_list.pop(word_index)
    else:
        text_out += string_list.pop(word_index - len(string))
print("".join(text_out))