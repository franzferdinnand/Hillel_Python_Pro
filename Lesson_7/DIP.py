import random
from faker import Faker


class Student:
    def __init__(self):
        self.rating = 0


class Teacher:
    def evaluate_student(self, student):
        student.rating += random.randint(5, 20)


class Results:
    def __init__(self):
        faked = Faker()
        self.student_name = faked.profile()['name']

    def result(self, student, teacher):
        student_one = student()
        teacher().evaluate_student(student_one)
        return f'{self.student_name}, {student_one.rating}'


if __name__ == '__main__':
    
    for st in range(10):
        table = Results()
        print(table.result(Student, Teacher))


