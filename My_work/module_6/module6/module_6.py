# ------------Лекция множественное наследование. Метод супер-------------


class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Привет, меня зовут {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


# human = Human('Денис')
# print(human.name)
student = Student('Макс', 'Urban', 'Питон1')
print(f'меня зовут {student.name}, я учусь в университете {student.place}')
# student.about()
print(Student.mro())
