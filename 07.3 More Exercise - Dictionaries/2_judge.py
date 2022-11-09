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
    command = input()
for contest, user_points in contests.items():
    for user, point in user_points.items():
        if user not in individual.keys():
            individual[user] = 0
        individual[user] += point
for key, value in contests.items():
    print(f"{key}: {len(value)} participants")
    num = 1
    for key1, value1 in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{num}. {key1} <::> {value1}")
        num += 1
print("Individual standings:")
num = 1
for name, total_points in sorted(individual.items(), key=lambda x: (-x[1], x[0])):
    print(f"{num}. {name} -> {total_points}")
    num += 1
