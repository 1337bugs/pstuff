def to_letters(grades):
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


class Journal:
    student_data = []

    def __init__(self, students):
        for dict in students:
            self.student_data.append(dict)


    def get_letter_grades(self, student_name):
        for dict in self.student_data:
            if student_name in dict["name"]:
                print("Grades of " + student_name +": ")
                print("Homework:", to_letters(dict["homework"]))
                print("Quizzes:", to_letters(dict["quizzes"]))
                print("Tests:", to_letters(dict["tests"]))
                print()

    def get_student_average(self, student_name):
        pass






    def print_data(self):
        for item in self.student_data:
            print(item)


def main():

    students = [
        {
          "name": "Lloyd",
          "homework": [90.0,97.0,75.0,92.0],
          "quizzes": [88.0,40.0,94.0],
          "tests": [75.0,90.0]
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
    #journal.print_data()
    print()

    #testing to_letters
    #
    #sample = [100.0, 92.0, 98.0, 100.0]
    #res = ""
    #res += to_letters(sample)
    #print(res)

    journal.get_letter_grades("Alice")



if __name__ == "__main__":
    main()
