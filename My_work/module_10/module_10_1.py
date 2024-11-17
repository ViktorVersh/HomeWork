"""
Задача "Потоковая запись в файлы"
"""
import threading  # Импорт библиотеки потоков
from time import sleep, time # Импорт из библиотеки time функции time и sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n') # Записываем строку в файл
            sleep(0.1) # Устанавливаем задержку по времени после записи строки
        print(f'Завершилась запись в файл {file_name}')
        return

start_time = time() # Запускаем счетчик времени для функции
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print(f'Время затраченное на работу функции {time() - start_time}') # подсчитываем и выводим затраченное время

start_time = time()  # Запускаем счетчик времени для потоков

#--------------Создаем потоки---------------------------
thread1 = threading.Thread(target=write_words, args= (10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

#--------------Запускаем потоки---------------------------
thread1.start()
thread2.start()
thread3.start()
thread4.start()

#--------------Закрываем потоки---------------------------
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print(f'Время затраченное на работу потоков {time() - start_time}') # подсчитываем и выводим затраченное время
