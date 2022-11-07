students_number = int(input())
student = {}
for num in range(students_number):
    student_name = input()
    student_grade = float(input())
    if student_name not in student.keys():
        student[student_name] = []
    student[student_name].append(student_grade)
for name, grades in student.items():
    averagegrade = sum(grades)/len(grades)
    if averagegrade >= 4.50:
        print(f"{name} -> {averagegrade:.2f}")
