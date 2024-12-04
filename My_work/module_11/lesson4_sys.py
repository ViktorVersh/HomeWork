import sys
from pprint import pprint


# pprint(dir(sys))

# Показывает путь к интерпретатору
# print(sys.executable)

# в какой операционной системе работаем
# print(sys.platform)


# версия интерпретатора
# print(sys.version)
# print(sys.version_info)


# def func(x):
#     if sys.version.split(' ')[0] == '3.12.7':
#         return x * 2
#     else:
#         raise Exception('Недопустимая версия')
#
# print(func(10))


# print(sys.argv)

# # словарь, который отображает имена всех загруженных модулей и объекты для загруженных модулей
# print(sys.modules)

# # Путь модуля, каталога где пайтон будет искать модули во время импорта
# print(sys.path)

# Псевдомодуль который содержит имена установленных в пайтон  объектов, модулей, функций
# print(__builtins__)
# pprint(dir(__builtins__))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(10000)
print(factorial(2000))
print(sys.getsizeof(factorial))
