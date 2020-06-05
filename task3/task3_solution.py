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
    # not universal
    def avg_grade(self, homework, quizzes, tests):
        grades = homework + quizzes + tests
        res = sum(grades)/len(grades)
        return f"{res:.2f}"

    def get_letter_grades(self, *args, throw_exception=False):
        for dict in self.student_data:
            if dict.get("name", 0) in args:
                print("Grades of " + dict.get("name", 0) + ": ")
                print("Homework:", self.to_letters(dict.get("homework", 0)))
                print("Quizzes:", self.to_letters(dict.get("quizzes", 0)))
                print("Tests:", self.to_letters(dict.get("tests", 0)))
            else:
                # if keyword specified, show error instead of skipping
                if throw_exception:
                    print("No student with such name in table")

    def get_student_average(self, *args, throw_exception=False):
        for dict in self.student_data:
            if dict.get("name", 0) in args:
                print("Average grade of", dict.get("name", 0), ":",
                      #adding 0 if no such key found, care
                      self.avg_grade(dict.get("homework", 0),
                                     dict.get("quizzes", 0),
                                     dict.get("tests", 0)))
                # debug
                # print(dict.get("name", 0) in (i for i in args))
            else:
                if throw_exception:
                    print("No student with such name in table")

    # to see the state of data
    def show_data(self):
        for data in self.student_data:
            print(data.values())

    def update_grade(self, student_name, throw_exception=False, **kwargs):
        for dict in self.student_data:
            if student_name in dict.get("name"):
                for new_work, new_grades in kwargs.items():
                    dict[new_work].extend(new_grades)
            else:
                if throw_exception:
                    print("No entry", student_name, "in table")


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

    # uncomment the following to test the task

    journal.get_letter_grades("Carl", "Alice", throw_exception=True)
    print()
    #journal.get_letter_grades("Carl", "Lloyd")
    #journal.get_student_average("Alice", "Tyler")
    print()

    #journal.get_student_average("Alice", "Carl", throw_exception=True)

    # journal.get_letter_grades("Tyler")
    # test_list = ["Tyler", "Lloyd", "Carl", "Alice"]
    # journal.get_student_average(*test_list, throw_exception=True)

    journal.update_grade("Carl", throw_exception=True,
                         homework=[100.0],
                         tests=[90.0, 91.0, 85.0])

    journal.update_grade("Alice", throw_exception=True,
                         homework=[100.0],
                         tests=[90.0, 91.0, 85.0])
    # journal.get_student_average("Lloyd")

    journal.show_data()


if __name__ == "__main__":
    main()
