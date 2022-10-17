from datetime import date


class Student:
    # STATE
    # name, age, subject, country, eye color, height, etc.
    def __init__(self, name: str, age: int):
        # instance variables
        self.name = name
        self.age = age

    # BEHAVIOR
    # instance methods
    def says(
        self, message
    ):  # self corresponds to this instance on which the method is called
        return f"{self.name.capitalize()} says {message}!"

    def studies(self, book):
        # You can call other instance methods using self.
        self.says("I'm studying...")
        # etc.

    # class methods (do not depend on a specific instance)
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = date.today().year - birth_year
        return cls(name, age)
