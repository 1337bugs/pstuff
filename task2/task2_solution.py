class Journal:

    student_data = []

    def __init__(self, students):
        self.student_data.append([ item for item in students ])

    def get_letter_grades(self, student_name):
        pass

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
    journal.print_data()



if __name__ == "__main__":
    main()
