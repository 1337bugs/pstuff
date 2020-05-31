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

    def inDict(self, name):
        found = False
        for dict in self.student_data:
            if name in dict.values():
                found = True
                return found
                break
        return found

    # getting info of 1 name
    def getDictInfo(self, name):
        for dict in self.student_data:
            if dict.get("name") == name:
                print("Grades of " + name + ": ")
                print("Homework:", self.to_letters(dict["homework"]))
                print("Quizzes:", self.to_letters(dict["quizzes"]))
                print("Tests:", self.to_letters(dict["tests"]))

    def get_letter_grades(self, *students, throw_exception=False):
        for name in students:
            if self.inDict(name):
                self.getDictInfo(name)
            else:
                # if keyword specified, show error instead of skipping
                if throw_exception:
                    print("No such name")

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

    journal.get_letter_grades("Carl", "Alice")
    #journal.get_student_average("Alice")

    #journal.inDict("Alice")
    #journal.getDictInfo("Carl")

    #journal.get_letter_grades("Tyler")
    #journal.get_student_average("Tyler")

    #journal.get_student_average("Lloyd")


if __name__ == "__main__":
    main()
