import math  # импортируем модуль math
from math import pi  # импортируем функцию pi


class Figure:
    sides_count = 0  # счетчик кол-ва сторон

    def __init__(self, __sides, __color):
        self.__sides = __sides  # кол-во сторон
        self.__color = __color  # цвет
        self.filled = False

    def get_color(self):
        return list(self.__color)  # возвращаем цвет

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:  # проверка цвета
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):  # проверка цвета
            self.__color = (r, g, b)  # установка цвета
        else:
            return False

    def __is_valid_sides(self, *sides):
        for i in sides:  # проверка кол-ва сторон
            if len(sides) == self.sides_count and isinstance(i, int) and i > 0:
                return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)  # возвращаем кол-во сторон

    def __len__(self):
        side_ = 0
        for i in list(self.__sides):  # перебор кол-ва сторон
            side_ += i
        return side_  # возвращаем кол-во сторон

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):  # проверка кол-ва сторон
            self.__sides = new_sides  # установка кол-ва сторон
        else:
            return False


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides * 2 * pi  # находим радиус
        self.__sides = sides

    def get_square(self):
        return (self.__radius ** 2) * pi  # вычисляем площадь круга


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(sides, color)

    def get_square(self):
        p = self.__sides * self.sides_count
        return math.sqrt(p * (p - self.__sides) * 3)  # вычисляем площадь треугольника


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__([sides] * self.sides_count, color)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3  # вычисляем объём куба


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
