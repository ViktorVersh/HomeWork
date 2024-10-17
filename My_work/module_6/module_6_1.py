class Animal:
    """
    Родительский класс Животные, содержит переменные живой - alive и сытый - fed
    """
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):  # функция кормления животного
        if not food.edible:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True


class Plant:
    """
    Родительский класс Растения, содержит переменную съедобный - edible
    """
    edible = False

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    """
    Дочерний класс Хищники
    """


class Mammal(Animal):
    """
    Дочерний класс Млекопитающие
    """


class Flower(Plant):
    """
    Дочерний класс Цветы
    """


class Fruit(Plant):
    """
    Дочерний класс Фрукты
    """
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
