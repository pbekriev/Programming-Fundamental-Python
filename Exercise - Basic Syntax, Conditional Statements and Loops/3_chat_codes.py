number_of_massages = int(input())

for loop in range (number_of_massages):
    code = int(input())
    if code == 88:
        word = "Hello"
    elif code == 86:
        word = "How are you?"
    elif code < 88 and code != 86:
        word = "GREAT!"
    else:
        word = "Bye."
    print(word)
