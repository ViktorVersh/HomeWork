"""
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
Задача "Банковские операции"
"""

import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            dep_count = random.randint(50, 500)
            self.balance += dep_count
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {dep_count}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            take_count = random.randint(50, 500)
            print(f'Запрос на {take_count}')
            if take_count <= self.balance:
                self.balance -= take_count
                print(f'Снятие: {take_count}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
