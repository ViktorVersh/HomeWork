import math


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color
        self.__filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            return False

    def __is_valid_sides(self, *sides):
        for i in sides:
            if len(sides) == self.sides_count and isinstance(i, int) and i > 0:
                return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        side = 0
        for i in list(self.__sides):
            side += i
        return side

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            return False


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        self.__radius = sides / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides

    def get_square(self):
        p = (self.__sides + self.__sides + self.__sides) / 2
        return round(math.sqrt(p * (p - self.__sides) * (p - self.__sides) * (p - self.__sides)), 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, [sides] * self.sides_count)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 100), 10)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(55, 62, 77)  # Изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

triangle1.set_sides(10, 20, 30)  # Изменится
print(triangle1.get_sides())

triangle1.set_color(260, 45, 20)  # Не изменится
print(triangle1.get_color())

print(triangle1.get_square())  # Проверка площади треугольника

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
