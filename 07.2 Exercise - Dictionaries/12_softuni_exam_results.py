# results = {}
# submissions = {}
# command = input()
# while command != "exam finished":
#     split_command = command.split("-")
#     if "banned" in command:
#         del results[split_command[0]]
#     else:
#         if split_command[0] not in results.keys() or results[split_command[0]] < split_command[2]:
#             results[split_command[0]] = split_command[2]
#
#         if split_command[1] not in submissions.keys():
#             submissions[split_command[1]] = 0
#         submissions[split_command[1]] += 1
#     command = input()
#
# print("Results:")
# for username, point in results.items():
#     print(f"{username} | {point}")
# print("Submissions:")
# for language, submissions_count in submissions.items():
#     print(f"{language} - {submissions_count}")


results = {}
submissions = {}
command = input()
while command != "exam finished":
    split_command = command.split("-")
    if "banned" in command:
        del results[split_command[0]]
    else:
        if split_command[0] not in results.keys():
            results[split_command[0]] = {}
            results[split_command[0]][split_command[1]] = split_command[2]
        if split_command[1] not in results[split_command[0]].keys() or results[split_command[0]][
            split_command[1]] < split_command[2]:
            results[split_command[0]][split_command[1]] = split_command[2]

        if split_command[1] not in submissions.keys():
            submissions[split_command[1]] = 0
        submissions[split_command[1]] += 1
    command = input()
print("Results:")
for username, point in results.items():
    for key, value in point.items():
        print(f"{username} | {value}")
print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")
