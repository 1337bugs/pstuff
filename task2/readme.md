## task2 OOP 

### context
In previous task we implemented simple journal based on dictionary. Now we want to be able to have multiple journals.

### task

Implement class `Journal` which will be able to do following tasks:
* `__init__` method, which will accept list of students and will save them
* get_letter_grades(self, student_name) - should return simple multiline text with task that student did and his grades as letters for every task in his dictionary
* get_student_average(self, student_name) - should return simple text with student overall average grade, result should look like `75.5` (try using build it methods/functions)

notes:
There is no need to dive too deep in OOP, we will continue on stuff like method types, inheritance and like that later.

### input data:
```python
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
```