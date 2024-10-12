class Human:
    def __init__(self, name, age): # self - указатель на самого себя, на объект например в нашем случае den или maxi
        self.name = name
        self.age = age
        self.say_info()


    def say_info (self):
        print(f'Привет меня зовут {self.name}, мне {self.age}')


    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')

    def __del__(self):
        print(f'{self.name} ушел')

    def __len__(self):
        return self.age

    def __lt__(self, other): # lt - Lower then - меньше чем
        return self.age < other.age

    def __gt__(self, other): # gt - Greater then - Больше чем
        return  self.age > other.age

    def __eq__(self, other): # Оператор равенства
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __str__(self):
        return f'{self.name}'


    
'''
объект это переменная созданная внутри класса, а класс это инструкция (план) в котором описаны какие характеристики,
способности есть у наших объектов
'''



den = Human('Денис', 22)
maxi = Human('Максим', 22)

if den:
    den.say_info()
print(den)
print(den < maxi)
print(den > maxi)
maxi.birthday()
print(den < maxi)
print(den > maxi)
print(den == maxi)
# print(len(den))
# print(den.name, den.age)
# print(maxi.name, maxi.age)
# print(den.name, den.age, maxi.name, maxi.age)
# den.say_info()
# maxi.say_info()
