## more OOP

### context
It's pretty hard now to work with list of dictionaries that we have as input data. And it doesn't support more subjects, so when it gets bigger it wold be even more problematic then uncomfortable.
So lets move from this complicated structures to more OOP. Now we need to define User class, and two inherited classes Student and Professor.
### task
You need to develop 3 new classes, and basically make everything work same way as it works now, but with classes instead of list of dicts.

In class `User` we should have:
* first_name (str)
* last_name (str)
* is_professor (bool) (where professors are True and students - False)
* all fields should be initialized on creation and can't be updatd

In class `Professor` we should have:
* academic_subjects (list) (names of those ones that that professor teaches)
* students_current_term (list) (list of `Student` objects which are studying from professor)
* all the fields can be initialized on creation and can be updated later

In class `Student` we should have:
* academic_subjects (dict) (which are for now are the same dict structure, we will develop `Subject` class and stuff like that later)
* professors_current_term (list) (list of `Student` objects which are studying from professor)
* all the fields can be initialized on creation and can be updated later

### notes:
If you think that classes miss some fields - updates are welcome \
As for existing functions:
* `avg_grade`, `get_letter_grades`, `get_student_average` should keep doing same thing, but now for all subjects separately
* `update_grade` should accept one more argument, which should contain subject name


### what to pay attention to:
(I also added new section with stuff that you should know in some way or another after completing task)

* python inheritance
* super()
* what it `Object` and `Type` classes in python and why are they so important
* Python MRO (Method Resolution Order)

### input data:

Students academic_subjects:
```python
# for Lloyd TheRock student:
{
    'math': {
      "homework": [90.0,97.0,75.0,92.0],
      "quizzes": [90.0,55.0,94.0],
      "tests": [75.0,90.0]
    },
    'physics':{
      "homework": [90.0,97.0,75.0,92.0],
      "quizzes": [88.0,40.0,94.0],
      "tests": [75.0,90.0]
    }
}
# for Alice Beyonce student:
{
    'english': {
      "homework": [80.0,100.0,66.0,72.0],
      "quizzes": [78.0,90.0,91.0],
      "tests": [80.0,90.0]
    },
    'science':{
      "homework": [100.0,97.0,85.0,82.0],
      "quizzes": [88.0,80.0,76.0],
      "tests": [90.0,60.0]
    }
}

# for Tyler Stalone student:
{
    'music': {
      "homework": [98.0,97.0,96.0,95.0],
      "quizzes": [89.0,60.0,95.0],
      "tests": [75.0,97.0]
    },
    'history':{
      "homework": [80.0,77.0,78.0,81.0],
      "quizzes": [88.0,77.0,96.0],
      "tests": [85.0,91.0]
    }
}

# for Barack Obama professor:
academic_subjects = ['music', 'history', 'english']

# for Tom Hanks professor:
academic_subjects = ['math', 'physics', 'science']

```
