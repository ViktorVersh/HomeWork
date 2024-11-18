import threading  # импортируем библиотеку потоков threading
import time  # импортируем библиотеку time


# ------------------создаем свой класс потоков------------------------------
class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):  # функция вывода времени
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1

    #  -----------------переопределяем метод run------------------------
    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')


# ------------------создаем потоки----------------------------------
thread1 = MyThread('thread1', 5, 1)
thread2 = MyThread('thread2', 3, 0.5)

thread1.start()
thread2.start()
