contest_data = {}
submissions = {}
command = input()
end_of_contests = False
while not end_of_contests:
    if command == "end of contests":
        end_of_contests = True
    else:
        contest_name, contest_pass = command.split(":")
        contest_data[contest_name] = contest_pass
    command = input()
while command != "end of submissions":
    contest, password, username, points_str = command.split("=>")
    point = int(points_str)
    if contest in contest_data.keys() and password == contest_data[contest]:
        if username not in submissions.keys():
            submissions[username] = {}
        if contest not in submissions[username].keys() or point > submissions[username][contest]:
            submissions[username][contest] = point
    command = input()
best_user = ""
best_user_total_points = 0
for key, value in submissions.items():
    if sum(value.values()) > best_user_total_points:
        best_user = key
        best_user_total_points = sum(value.values())
print(f"Best candidate is {best_user} with total {best_user_total_points} points.\nRanking:")
for key, value in sorted(submissions.items()):
    print(key)
    for key1, value1 in sorted(value.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {key1} -> {value1}")
