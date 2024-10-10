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
'''
объект это переменная созданная внутри класса, а класс это инструкция (план) в котором описаны какие характеристики,
способности есть у наших объектов
'''



den = Human('Денис', 22)
maxi = Human('Максим', 25)
maxi.birthday()
print(den.name, den.age)
print(maxi.name, maxi.age)
print(den.name, den.age, maxi.name, maxi.age)
den.say_info()
maxi.say_info()
