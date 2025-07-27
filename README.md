# 🐱 Cat Class in Python

This project demonstrates basic Object-Oriented Programming (OOP) concepts in Python using a `cat` class.  
It allows the user to create multiple cat objects by taking input and then displays their information and checks if the cat is a senior.

---

## 🚀 Features

- Uses Python classes and constructors
- Accepts user input for multiple cat objects
- Displays cat information (name, age, breed)
- Checks if a cat is a senior (age > 8)

---

## 📂 Code Overview

```python
class cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print(f"Meow! My name is {self.name}")

    def catinfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old and " + self.breed + " breed")

    def is_senior(self):
        if self.age > 8:
            return "True"
        else:
            return "False"
