import pdb

class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student, grade):
        self.grades[student] = grade

    def get_grade(self, student):
        if self.grades.get(student) is None:
            return -1
        return self.grades[student]

grades = StudentGrades()

grades.add_grade("Alice", 85)
grades.add_grade("Bob", 90)

print("Grade for Charlie:", grades.get_grade("Charlie"))
