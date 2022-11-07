results = {}
submissions = {}
command = input()
while command != "exam finished":
    current_command = command.split("-")
    if "banned" in current_command:
        del results[current_command[0]]
    else:
        username, language, points = current_command
        if (username not in results.keys()) or (int(results[username]) < int(points)):
            results[username] = [points]
        # if results[current_command[0]] < int(current_command[2]):
        #     results[current_command[0]] = [current_command[2]]
    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1

print(results)
print(submissions)
