from student import Student

student1 = Student('George Orwell')
student2 = Student('Zach Zak')
student3 = Student('Lady Gaga')

student1.add_grades([89, 70, 55, 60, 29])
student2.add_grades([69, 100, 99, 45, 76])
student3.add_grades([80, 80, 79, 43, 91])

student1.print_grade_report()
print("best grade", student1.find_max_grade(), "lowest grade", student1.find_min_grade())
print("Average grade is", student1.calculate_avg_grade(), "\n")

student2.print_grade_report()
print("best grade", student2.find_max_grade(), "lowest grade", student2.find_min_grade())
print("Average grade is", student2.calculate_avg_grade(), "\n")

student3.print_grade_report()
print("best grade", student3.find_max_grade(), "lowest grade", student3.find_min_grade())
print("Average grade is", student3.calculate_avg_grade())
