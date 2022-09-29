number_of_string = int(input())
word = input()
list_with_all_word = []
list_with_word = []

for _ in range(number_of_string):
    string = input()
    list_with_all_word.append(string)
    if word in string:
        list_with_word.append(string)

print(list_with_all_word)
print(list_with_word)
