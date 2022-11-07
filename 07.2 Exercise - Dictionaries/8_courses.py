courses = {}
command = input()
while command != "end":
    current_command = command.split(" : ")
    course_name = current_command[0]
    student_name = current_command[1]
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()
for course_name, student_name in courses.items():
    print(f"{course_name}: {len(student_name)}")
    for name in student_name:
        print(f"-- {name}")
