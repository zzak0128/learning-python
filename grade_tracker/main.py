from student import Student

students = [Student('George Orwell'), Student('Zach Zak'), Student('Lady Gaga')]
students[0].add_grades([89, 70, 55, 60, 29])
students[1].add_grades([69, 100, 99, 45, 76])
students[2].add_grades([80, 80, 79, 43, 91])

for student in students:
    student.print_grade_report()
    print("best grade", str(student.find_max_grade()), "lowest grade", str(student.find_min_grade()))
    print("Average grade is", student.calculate_avg_grade(), "\n")

with open("./grade_reports.txt", "a") as file:
    for student in students:
        student.write_grade_report(file)
        file.write(
            "best grade " + str(student.find_max_grade()) + " lowest grade " + str(student.find_min_grade()) + "\n")
        file.write("Average grade is " + str(student.calculate_avg_grade()) + "\n")
