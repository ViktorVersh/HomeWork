"""
Лекция "Наследование классов. Зачем нужно наследование"
"""


class Human:
    head = True

    def __init__(self, name):
        self.name = name

    def hello_say(self):
        print(f'Здравствуйте')


class Student(Human):
    head = False

    def about(self):
        print('Я студент')


class Teacher(Human):
    pass


student = Student('Денис')
teacher = Teacher('Сергей Петрович')
student.hello_say()
print(student.name)
student.about()
teacher.hello_say()
print(teacher.name)
print(student.head)
print(teacher.head)
