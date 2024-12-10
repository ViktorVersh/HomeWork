"""
Задача "Магические здания":
"""
from time import sleep  # из модуля time импортируем задержку времени sleep


class House:
    """
    Класс House обладает атрибутами name - имя объекта и number_of_floor - этажность объекта,
    а также методом go_to - поездка на лифте на указанный этаж: new_floor, должен выводить на
    экран цифры от 1 до new_floor, и специальными магическими методами __len__ и __str__, которые
    соответственно выводят на экран этажность здания(__len__) и название объекта (__str__)
    """

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def go_to(self, new_floor=int):
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                sleep(0.4)
                print(i)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
