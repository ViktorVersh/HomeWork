import requests
from pprint import pprint
import inspect

some_string = 'Я строчка'
some_number = 45
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('Мои параметры: ' + param, + param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_metod(self, value):
        self.attribute_1 = value
        print(self.attribute_1)

some_object = SomeClass()


# Пример 1 - Функция hasattr() - проверка на существования  атрибута
#
# attr_name = 'attribute_2'
# pprint(hasattr(some_object, attr_name))
# pprint(hasattr(some_object, 'attribute_1'))
# pprint(dir(some_object))

#  Пример 2 Получение атрибута функция getattr()
#
# pprint(getattr(some_object, 'attribute_1'))
# pprint(getattr(some_object, 'attribute_2', 'этого не может быть'))
#
# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))

# Пример 3 функция callable() - проверка на то, можем ли мы вызвать этот объект

# print(callable(some_number))
# print(callable(some_list))
# print(callable(some_object.attribute_1))
# print(callable(some_object.some_class_metod))


# Пример 4 функция isinstance() - определяем является ли объект экземпляром указанного класса

# print(isinstance(some_number, int))
# print(isinstance(some_number, str))
# print(isinstance(some_number, SomeClass))
# print(isinstance(some_object, SomeClass))


# Модуль ispect - https://docs.python.org/3/library/inspect.html
# собирает удобные методы и классы для отображения интроспективной информации
# Пример 5 самые употребляемые функции

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)
