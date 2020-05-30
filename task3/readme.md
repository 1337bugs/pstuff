## *args, **kwargs, named params

### context
In previous task we figured out some OOP and added methods to out new Journal class. Now we can try figuring out a lot of other stuff alongside practicing OOP all the time.  \
Now lets make this class a bit more dynamic. We will add ability for professor to gather info about multiple students at once, update students list and get more info on his input.

### task

In class `Journal`:
* update method `get_letter_grades` and `get_student_average` so now they can accept `*args` instead of one `student_name` and print info for multiple students
* update method `get_letter_grades` and `get_student_average` with named argument `throw_exception` with default value to `False`. When `throw_exception` changed to `True` instead of silently skipping student name we should print an errot that that name was not found.
* add new method `update_grade`, which accepts `student_name`, `throw_exception` and `**kwargs`. What `student_name` and `throw_exception` may be clear by this point; `**kwargs` should accept similar to out input data structure, like `{"name": "Alice", "tests":[100.0]}`. But, instead of just changing existing list to passed one it should update the one that we already have(try doing it without loops, just with built in methods)

### input data:
Is the same as in task2
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