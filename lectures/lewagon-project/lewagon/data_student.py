from lewagon.student import Student


# class ChildClass(ParentClass):
# class SubClass(SuperClass):
class DataStudent(Student):
    topic = "data science"

    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty
