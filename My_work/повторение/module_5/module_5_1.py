"""
Задача "Developer - не только разработчик":
"""
from time import sleep  # из модуля time импортируем задержку времени sleep


class House:
    """
    Класс House обладает атрибутами name - имя объекта и number_of_floor - этажность объекта,
    а также методом go_to - поездка на лифте на указанный этаж: new_floor, должен выводить на
    экран цифры от 1 до new_floor.
    """

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor=int):
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                sleep(0.4)
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
print()
h2.go_to(10)
