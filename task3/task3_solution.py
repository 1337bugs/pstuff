class Journal:

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
    """
    def get_letter_grades(self, *students, throw_exception=True):
        for dict in self.student_data:
            if dict.get(name) not in students:
            for name in students:
                print(name)
                if name in dict["name"]:
                    print("Grades of " + name + ": ")
                    print("Homework:", self.to_letters(dict["homework"]))
                    print("Quizzes:", self.to_letters(dict["quizzes"]))
                    print("Tests:", self.to_letters(dict["tests"]))
                else:
                    print("Name not found")
                continue




    def get_letter_grades(self, *students, throw_exception=False):
        students_iter = iter(students)
        for name in students:
            for i in range(len(self.student_data)):
                if throw_exception:
                    if name in self.student_data[i].get("name"):
                        print("Grades of " + name + ": ")
                        print("Homework:", self.to_letters(self.student_data[i]["homework"]))
                        print("Quizzes:", self.to_letters(self.student_data[i]["quizzes"]))
                        print("Tests:", self.to_letters(self.student_data[i]["tests"]))
                    else:
                        print("Name not found")
                        next(students_iter)
                else:
                    if name in self.student_data[i].get("name"):
                        print("Grades of " + name + ": ")
                        print("Homework:", self.to_letters(self.student_data[i]["homework"]))
                        print("Quizzes:", self.to_letters(self.student_data[i]["quizzes"]))
                        print("Tests:", self.to_letters(self.student_data[i]["tests"]))
    """


    def inDict(self, name):
        for i in range(len(self.student_data)):
            if name in self.student_data[i]["name"]:
                print("da")
                return True
            else:
                print(name)
                print("nyet")
                return False

    def getDictInfo(self, name):
        for dict in self.student_data:
            if dict.get(name) != None or dict.get(name) == name:
                print("Grades of " + name + ": ")
                print("Homework:", self.to_letters(dict.get("homework")))
                print("Quizzes:", self.to_letters(dict.get("quizzes")))
                print("Tests:", self.to_letters(dict.get("tests")))
            else:
                print("nichego")

    def get_letter_grades(self, *students, throw_exception=False):
        for name in students:
            if self.inDict(name):
                print(name)
                self.getDictInfo(name)

    """
    def get_letter_grades(self, *students, throw_exception=False):
        for name in students:
            if name in self.student_data
"""


    def get_student_average(self, *students, throw_exception=False):
        for dict in self.student_data:
            for name in students:
                if name in dict["name"]:
                    print("Average grade of", name, ":", "{0:5.2f}".format(
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

    journal.get_letter_grades("Carl", "Alice", "Tyler", throw_exception=True)
    #journal.get_student_average("Alice")

    #journal.inDict("Carl")
    #journal.getDictInfo("Carl")

    #journal.get_letter_grades("Tyler")
    #journal.get_student_average("Tyler")

    #journal.get_student_average("Lloyd")


if __name__ == "__main__":
    main()
