name = input()
command = True
while name != "Welcome!":
    if name == "Voldemort":
        command = False
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if command:
    print("Welcome to Hogwarts.")
