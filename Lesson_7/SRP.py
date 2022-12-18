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
        self.good_stud_rating = random.randint(5, 10)
        self.bad_stud_rating = random.randint(1, 5)

    def evaluate_student(self, student):
        if student.books > 0:
            student.rating += self.good_stud_rating
        else:
            student.rating += self.bad_stud_rating


if __name__ == '__main__':
    student1 = Student()
    student2 = Student()
    teacher = Teacher()
    student1.read_book()
    student1.read_book()
    teacher.evaluate_student(student1)
    teacher.evaluate_student(student2)
    print(student1.name, student1.last_name, student1.rating)
    print(student2.name, student2.last_name, student2.rating)
