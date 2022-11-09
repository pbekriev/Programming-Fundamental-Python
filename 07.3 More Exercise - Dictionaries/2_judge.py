contests = {}
individual = {}
command = input()
while command != "no more time":
    username, contest, points_str = command.split(" -> ")
    points = int(points_str)
    if contest not in contests.keys():
        contests[contest] = {}
    if username not in contests[contest].keys() or contests[contest][username] < points:
        contests[contest][username] = points
    if username not in individual.keys():
        individual[username] = points
    individual[username] += points
    command = input()

for key, value in contests.items():
    print(f"{key}: {len(value)} participants")
    for key1, value1 in value.items():
        num = 1
        print(f"{num}. {key1} <::> {value1}")
