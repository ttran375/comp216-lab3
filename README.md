# Lecture 3

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ttran375/comp216-lab3/blob/main/src/main.ipynb)

## Question 1

A user profile class was introduced into an application
based on the following definition:

```python
class User:
    registered_user_count = 0

    def __init__(self, first_name, last_name, age, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.postal_code = postal_code

    def registered(self, status):
        self.registered = status
        User.registered_user_count += 1
```

Update the relevant methods to ensure:

- The first_name and last_name attributes are supplied as strings that
    only contain alphabetical characters. If not, raise a Value Error.

- The age attribute is supplied as an integer and the age \> 13. If
    not, raise a Value Error.

- The postal_code attribute is supplied as that only contains
    alphanumerical characters. If not, raise a Value Error and
    auto-populate the attribute with the value: ‘X0X0X0’.

## Question 2

Use the following list of tuples that contains and scores of
students.

```python
students_scores = [
    ("Alice James", 85),
    ("Adam Bonson", 90),
    ("Matt Fowler", 78),
    ("David Curry", 92),
    ("Eva Porter", 80),
    ("Azure Kelsey", 79),
    ("Billie Jose", 64),
    ("Willian Maxime", 86),
]
```

Create a dictionary that includes high achieving (or honour) students
represented as key-value pairs:

- Keys must only include the first initial of the first name and full
    last name

- Values must only include scores that are 80% and higher

The expected output is the following:

```python
honour_students = {
    "A. James": 85,
    "A. Bonson": 90,
    "D. Curry": 92,
    "E. Porter": 80,
    "W. Maxime": 86,
}
```

## Question 3

Given the range object (below), create a single line
statement that utilizes a map(), filter() and lambda functions to
achieve the following:

- Filter the list to include only the even numbers.

- Square each of the filtered even numbers.

Use the following as the input: `numbers = range(1, 75, 3)`.

Afterwards, implement the same logic utilizing for loops and compare the
difference in the compute time between the two approaches.
