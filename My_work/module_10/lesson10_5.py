from threading import Thread, Event
from time import sleep


def first_work():
    print(f'Первый рабочий приступил к выполнению своей задачи')
    event.wait()
    print(f'Первый рабочий продолжил выполнять свою задачу')
    sleep(5)
    print(f'Первый рабочий закончил выполнять свою задачу')


def second_work():
    print(f'Второй рабочий приступил к выполнению своей задачи')
    sleep(10)
    print(f'Второй рабочий закончил выполнять свою задачу')
    event.set()


event = Event()

thread1 = Thread(target=first_work)
thread2 = Thread(target=second_work)
thread1.start()
thread2.start()
