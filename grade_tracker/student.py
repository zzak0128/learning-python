class Student:
    def __init__(self, name):
        self.name = name
        self.gradebook = []

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            print("Invalid Grade, must be between 0 and 100")
        else:
            self.gradebook.append(grade)

    def add_grades(self, grades):
        for grade in grades:
            self.add_grade(grade)

    def calculate_letter_grade(self, grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80 and grade < 90:
            return 'B'
        elif grade >= 70 and grade < 80:
            return 'C'
        elif grade >= 60 and grade < 70:
            return 'D'
        else:
            return 'F'

    def calculate_avg_grade(self):
        return self.calculate_letter_grade((sum(self.gradebook) / len(self.gradebook)))

    def calculate_final_grade(self):
        grade_sum = sum(self.gradebook)
        grade_max = len(self.gradebook)
        grade_calc = grade_sum / grade_max
        return self.calculate_letter_grade(grade_calc)

    def find_max_grade(self):
        return max(self.gradebook)

    def find_min_grade(self):
        return min(self.gradebook)

    def print_grade_report(self):
        print(self.name.upper())
        for grade in self.gradebook:
            print(grade, "/", 100, "--", self.calculate_letter_grade(grade))

    def write_grade_report(self, file):
        file.write(self.name.upper() + "\n")
        for grade in self.gradebook:
            file.write(str(grade) + " / " + "100 -- " + self.calculate_letter_grade(grade) + "\n")
