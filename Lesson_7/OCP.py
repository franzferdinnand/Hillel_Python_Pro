import random
from faker import Faker


class Student:

    def __init__(self):
        faker = Faker()
        self.name = faker.first_name()
        self.last_name = faker.last_name()
        self.books = 0
        self.rating = 0

    def read_book(self):
        self.books += 1


class Teacher:
    def __init__(self):
        faker = Faker()
        self.name = faker.first_name()
        self.last_name = faker.last_name()
        self.good_stud = random.randint(5, 10)
        self.bad_stud = random.randint(1, 5)

    def evaluate_student(self, student):
        if student.books > 0:
            student.rating += self.good_stud
        else:
            student.rating += self.bad_stud


class Professor(Teacher):
    def __init__(self):
        super().__init__()
        self.good_stud = random.randint(50, 100)
        self.bad_stud = random.randint(1, 49)



student1 = Student()
student2 = Student()
teacher = Teacher()
student1.read_book()
student1.read_book()
teacher.evaluate_student(student1)
teacher.evaluate_student(student2)
print(student1.name, student1.last_name, student1.rating)
print(student2.name, student2.last_name, student2.rating)

student3 = Student()
student4 = Student()
teacher2 = Professor()
student3.read_book()
student3.read_book()
teacher2.evaluate_student(student3)
teacher2.evaluate_student(student4)
print(student3.name, student3.last_name, student3.rating)
print(student4.name, student4.last_name, student4.rating)
