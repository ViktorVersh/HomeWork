# ---------------Задача "Функциональное разнообразие"---------------------
from random import choice  # Импортируем из библиотеки random функцию choice


class MysticBall:
    """
    Класс имитирующий магический шар.
    При вызове объекта класса, будет возвращать случайное слово из списка.
    """

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))  # Сравниваем символы строки и выводим результат True/False


def get_advanced_writer(file_name):  # Функция создающая файл(если его нет) и функцию для записи в него
    def write_everything(*data_set):  # Функция для записи в файл
        with open(file_name, 'w', encoding='utf-8') as f:  # Открываем файл
            for i in data_set:  # проходим по данным
                f.write(str(i) + '\n')  # записываем в файл

    return write_everything  # Возвращаем функцию


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть')
print(first_ball())
print(first_ball())
print(first_ball())
