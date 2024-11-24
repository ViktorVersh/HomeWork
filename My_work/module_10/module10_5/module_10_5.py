"""
Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
Задача "Многопроцессное считывание"
"""
import multiprocessing
import time
import datetime
from threading import Thread


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for i in file:
            all_data.append(i)


filenames = [f'./file {number}.txt' for number in range(1, 5)]  # создаем список имен файлов

# --------------------------------Линейный вызов------------------------------------
# start_time = time.time()
#
# thread1 = Thread(target=read_info(filenames[0]))
# thread2 = Thread(target=read_info(filenames[1]))
# thread3 = Thread(target=read_info(filenames[2]))
# thread4 = Thread(target=read_info(filenames[3]))
#
# end_time = time.time()
#
# res = end_time - start_time  # # время выполнения в секундах
# result = str(datetime.timedelta(seconds=res))  # # время выполнения в формате 00:00:00.000
# print(f'{result} (линейный)')  # вывод результата

# ------------------------------Многопроцессный вызов --------------------------------
if __name__ == '__main__':
    start_time = time.time()

    with multiprocessing.Pool(5) as pool:
        pool.map(read_info, [*filenames])

    end_time = time.time()

    res = end_time - start_time  # время выполнения в секундах
    result = str(datetime.timedelta(seconds=res))  # время выполнения в формате 00:00:00.000
    print(f'{result} (многопроцессный)')  # вывод результата
