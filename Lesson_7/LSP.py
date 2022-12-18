import random
from faker import Faker


class Person:

    def __init__(self):
        faked = Faker()
        self.name = faked.first_name()
        self.last_name = faked.last_name()
        self.books = 1

    def read_books(self):
        self.books += 1

    def calculate_books(self):
        return self.books


class Student(Person):

    def read_books(self):
        self.books += 2


class Teacher(Person):

    def read_books(self):
        self.books += 5


good_student = Student()
smart_teacher = Teacher()

good_student.read_books()
smart_teacher.read_books()

print(smart_teacher.name, smart_teacher.last_name, smart_teacher.calculate_books())
print(good_student.name, good_student.last_name, good_student.calculate_books())
