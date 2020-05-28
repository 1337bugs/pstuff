class Journal:
    student_data = []

    def __init__(self, students):
        self.student_data = students

    def to_letters(self, grades):
        res = ""
        for grade in grades:
            if grade >= 95.0:
                res += "A"
            elif grade >= 85.0:
                res += "B"
            elif grade >= 75.0:
                res += "C"
            elif grade >= 65.0:
                res += "D"
            elif grade >= 60.0:
                res += "E"
            elif grade < 60.0:
                res += "F"
            res += " "
        return res.strip()

    # calc overall average grade
    def avg_grade(self, homework, quizzes, tests):
        grades = homework + quizzes + tests
        res = sum(grades)/len(grades)
        return res

    def get_letter_grades(self, student_name):
        for dict in self.student_data:
            if student_name in dict["name"]:
                print("Grades of " + student_name + ": ")
                print("Homework:", self.to_letters(dict["homework"]))
                print("Quizzes:", self.to_letters(dict["quizzes"]))
                print("Tests:", self.to_letters(dict["tests"]))

    def get_student_average(self, student_name):
        for dict in self.student_data:
            if student_name in dict["name"]:
                print("Average grade of", student_name, ":", "{0:5.2f}".format(
                    self.avg_grade(dict["homework"],
                                   dict["quizzes"],
                                   dict["tests"])))


def main():

    students = [
        {
          "name": "Lloyd",
          "homework": [90.0, 97.0, 75.0, 92.0],
          "quizzes": [88.0, 40.0, 94.0],
          "tests": [75.0, 90.0]
        },
        {
          "name": "Alice",
          "homework": [100.0, 92.0, 98.0, 100.0],
          "quizzes": [82.0, 83.0, 91.0],
          "tests": [89.0, 97.0]
        },
        {
          "name": "Tyler",
          "homework": [0.0, 87.0, 75.0, 22.0],
          "quizzes": [0.0, 75.0, 78.0],
          "tests": [100.0, 100.0]
        }
    ]

    journal = Journal(students)
    print()

    journal.get_letter_grades("Alice")
    journal.get_student_average("Alice")

    journal.get_letter_grades("Tyler")
    journal.get_student_average("Tyler")

    journal.get_student_average("Lloyd")


if __name__ == "__main__":
    main()
