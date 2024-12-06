import requests
from pprint import pprint


some_string = 'Я строчка'
some_number = 45
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('Мои параметры: ' + param + param_2)

class SomeClass:
    def __init__(self):
        self.atribute_1 = 27

    def some_class_metod(self, value):
        self.atribute_1 = value
        print(self.atribute_1)

some_object = SomeClass()
func = some_function

# Пример 1 - Атрибут класса __name__

# print(some_function.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# print(func.__name__)

#
# # Пример 2 узнаем тип объекта type()
#
# print(type(some_function))
# print(type(SomeClass))
# print(type(func))
# print(type(some_number))
# print(type(some_number) is int)
# print(type(some_number) is str)
# print(type(some_number) is list)
#
# print(type(requests))
# print(type(requests.get))

 # Пример 3 функция dir
 # функция dir() возвращает отсортированный список атрибутов и методов для указанного объекта
 # который может быть объявленной переменной или функцией
pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_object))
# pprint(dir(some_object))
# pprint(dir(SomeClass))
# pprint(dir(requests))
# pprint(dir())

# help(requests)
# help(requests.get)