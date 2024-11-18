"""
Цель: научиться создавать классы наследованные от класса Thread.
Задача "За честь и отвагу!"
"""
# импортируем библиотеки
import threading
from threading import Thread
from time import sleep


class Knight(Thread):  # создаем класс и наследуемся от класса Thread
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.x = 100  # счетчик воинов

    def run(self):  # переопределяем метод run
        print(f'{self.name}, на нас напали')
        my_timer = 0  # счетчик дней
        while self.x > 0:
            my_timer += 1
            self.x -= self.power  # уменьшаем счетчик воинов за 1 день
            print(f'{self.name} сражается {my_timer} дней(дня)..., осталось {self.x} воинов')
            sleep(1)

        print(f'{self.name} одержал победу спустя {my_timer} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)  # создаем поток
second_knight = Knight("Sir Galahad", 20)  # создаем поток

first_knight.start()  # запускаем поток
sleep(0.1)  # смещаем потоки по времени, чтобы не склеивались строчки разных потоков
second_knight.start()  # запускаем поток

first_knight.join()  # завершаем первый поток
second_knight.join()  # завершаем второй поток
