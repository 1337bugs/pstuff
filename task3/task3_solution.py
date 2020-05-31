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
    def avg_grade(self, grades):
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

    def get_letter_grades(self, *students, throw_exception=False):
        for name in students:
            # if name is present in dictionaries, do stuff
            if self.inDict(name):
                for dict in self.student_data:
                    if dict.get("name") == name:
                        print("Grades of " + name + ": ")
                        temp = dict.copy()
                        temp.pop("name")
                        for work, grades in temp.items():
                            print(work, self.to_letters(grades))

                        # obsolete code, for testing purposes
                        #
                        # print("Homework:", self.to_letters(dict["homework"]))
                        # print("Quizzes:", self.to_letters(dict["quizzes"]))
                        # print("Tests:", self.to_letters(dict["tests"]))
            else:
                # if keyword specified, show error instead of skipping
                if throw_exception:
                    print("No entry", name, "in table")

    def get_student_average(self, *students, throw_exception=False):
        for name in students:
            # if name is present in dictionaries, do stuff
            if self.inDict(name):
                for dict in self.student_data:
                    if dict.get("name") == name:
                        temp = dict.copy()
                        temp.pop("name")
                        # there might be an overkill here or an easier way
                        # to pass list of values to avg_grade
                        list = []
                        for values in temp.values():
                            list.extend(values)
                        print("Average grade of", name, ":",
                              "{0:5.2f}".format(self.avg_grade(list)))

            else:
                # if keyword specified, show error instead of skipping
                if throw_exception:
                    print("No entry", name, "in table")

    # to see the state of data
    def test(self):
        for data in self.student_data:
            print([value for key, value in data.items()])

    def update_grade(self, student_name, throw_exception=False, **kwargs):
        if self.inDict(student_name):
            for dict in self.student_data:
                # seems like im breaking DRY next line
                if dict.get("name") == student_name:
                    for new_work, new_grades in kwargs.items():
                        for work, grades in dict.items():
                            if work in new_work:
                                grades.extend(new_grades)
        else:
            # if keyword specified, show error instead of skipping
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

    # journal.get_letter_grades("Carl", "Alice")
    # journal.get_student_average("Alice")

    # journal.inDict("Alice")
    # journal.get_dict_data("Carl")

    # journal.get_letter_grades("Tyler")
    # test_list = ["Tyler", "Lloyd", "Carl", "Alice"]
    # journal.get_student_average(*test_list, throw_exception=True)

    journal.update_grade("Carl", throw_exception=True,
                         homework=[100.0],
                         tests=[90.0, 91.0, 85.0])

    journal.update_grade("Alice",
                         homework=[100.0],
                         tests=[90.0, 91.0, 85.0])
    # journal.get_student_average("Lloyd")
    journal.test()


if __name__ == "__main__":
    main()
