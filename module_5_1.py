class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floors):
        if new_floors < 1 or new_floors > self.number_of_floors:
            print('"Такого этажа не существует"')
        else:
            for i in range(1, new_floors + 1):
                print(i)


h1 = House('ЖК "Горский"', 30)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
