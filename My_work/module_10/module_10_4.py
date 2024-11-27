"""
Цель: Применить очереди в работе с потоками, используя класс Queue.
Задача "Потоки гостей в кафе"
"""
from threading import Thread
import time
import random
import queue


class Table:  # класс столы
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):  # класс гостя наследуется от Thread
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:  # класс кафе
    def __init__(self, *args):
        self.tables = args
        self.queue = queue.Queue()
        self.guest = guests

    def guest_arrival(self, *guest):  # функция приема гостей
        for guest in guest:
            if any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        guest.start()
                        break
            else:
                self.queue.put(guest)  # добавление гостя в очередь
                print(f'{guest.name} в очереди')
                guest.start()

    def discuss_guests(self):
        while True:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()  # получение гостя из очереди
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
            if all(table.guest is None for table in self.tables) and self.queue.empty():
                break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria',
                'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
