year = int(input())

command = False

while not command:
    year += 1
    set_year = set()
    for loop in range(len(str(year))):
        set_year.add(str(year)[loop])

        command = len(set_year) == len(str(year))

print(year)
