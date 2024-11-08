# ------------------Почему функция это объект---------------------------
# def get_russia_names():
#     #  print(['Иван', 'Василий', 'Пётр', 'Дмитрий'])
#     return ['Иван', 'Василий', 'Пётр', 'Дмитрий']
#
#
# #  get_russia_names()
# #  print(type(get_russia_names))
#
# print(get_russia_names.__name__)
# my_func = get_russia_names
#
# print(my_func())
# print(my_func.__name__)


# ------------------- с функцией можно работать как с обычным объектом ------------------


# def get_russia_names():
#     return ['Иван', 'Василий', 'Пётр', 'Дмитрий']
#
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harri', 'Joni']
#
# name_getters = [get_russia_names, get_british_names]
#
# for name_getter in name_getters:
#     print(name_getter())
#

# ----------------функции высшего порядка(принимающие на вход другие функции с аргументами -----------------------

#
# def adder(args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# def multiplier(args):
#     res = 1
#     for i in args:
#         res *= i
#     return res
#
#
# def process_number(numbers, function):
#     result = function(numbers)
#     print(f'Получилось {result}')
#
# my_numbers = [1,2,3,4,5,6,7,8,9]
#
# process_number(numbers=my_numbers, function=adder)
# process_number(numbers=my_numbers, function=multiplier)

# -------------------- функция map -----------------------------

# def mul_by(x):
#     return x * 2
#
#
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# result = map(mul_by, my_numbers)
#
# print(result)
# print(list(result))

# --------------- функция filter --------------------------------


def is_odd(x):
    return x % 2


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = filter(is_odd, my_numbers)

print(result)
print(list(result))
