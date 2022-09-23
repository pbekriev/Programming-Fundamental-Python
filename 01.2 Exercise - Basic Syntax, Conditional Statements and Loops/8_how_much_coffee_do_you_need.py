command = ""
coffe_counter = 0
while command != "END":
    command = input()
    if command.lower() == "coding"\
        or command.lower() == "dog"\
        or command.lower() == "cat"\
        or command.lower() == "movie":
        if command.islower():
            coffe_counter += 1
        else:
            coffe_counter += 2
if coffe_counter > 5:
    print("You need extra sleep")
else:
    print(coffe_counter)