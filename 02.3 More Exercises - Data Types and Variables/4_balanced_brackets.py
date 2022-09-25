lines = int(input())

balanced = True
last_bracket = ''

for _ in range(lines):

    string_input = input()

    if string_input not in ['(', ')']:
        continue

    if last_bracket == '' and string_input == ')' or last_bracket == string_input:
        balanced = False
        break

    last_bracket = string_input

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
