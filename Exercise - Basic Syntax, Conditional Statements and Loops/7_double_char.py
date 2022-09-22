string = ""
while string != "End":
    string = input()
    word = ""
    if string == "SoftUni":
        continue
    elif string != "End":
        for letter in string:
            word += letter * 2
        print(word)
