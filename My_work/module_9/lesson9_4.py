# my_func = lambda x: x*10
# print(my_func(42))
# print(type(my_func))
#====================================================================================
# my_numbers = [1, 4, 5, 3, 6, 2]
#
# result = map(lambda x: x+10, my_numbers)
# print(list(result))

#=====================================================================================
# my_numbers = [1, 4, 5, 3, 6, 2]
# my_numbers2 = [2, 4, 7, 8, 9, 2]
# my_func = lambda x, y: x+y, my_numbers, my_numbers2
# print(type(my_func))

# ========================================================================================
# my_func = lambda x: x**2
# print(my_func(40))
# print(type(my_func))
# print(my_func.__name__)
# =======================================================================================
#------------------------Функции на лету---------------------------------------

# def get_multiplier_1(n):
#     if n == 2:
#         def multiplier(x):
#             return x**2
#     elif n ==3:
#         def multiplier(x):
#             return x**3
#     else:
#         raise Exception ('Я могу создавать множители только 2 и 3')
#     return multiplier
#
# my_number = [2, 4, 3, 6, 5, 7, 8]
#
# by2 = get_multiplier_1(2)
# by3 = get_multiplier_1(3)
#
# result1 = map(by2, my_number)
# result3 = map(by3, my_number)
#
# print(list(result1))
# print(list(result3))

#=======================================================================================

# def get_multiplier_2(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
# by_5 = get_multiplier_2(5)
# print(by_5(x=43))
# my_numbers = [2, 4, 3, 5, 6]
#
# by_10 = get_multiplier_2(10)
# print(list(map(by_10, my_numbers)))
#
# by_25 = get_multiplier_2(25)
# print(list(map(by_25, my_numbers)))

#=======================================================================================
#---------------------Пример №5 что не стоит передавать в аргументы функции ----------------
#----------------------изменяемые объекты и замыкать их------------------------------------
# from pprint import pprint
#
# def matrix(some_list):
#
#     def multi_column(x):
#         res = []
#         for i in some_list:
#             res.append(i * x)
#         return res
#
#     return multi_column
#
#
# my_numbers = [2, 3, 5, 7, 6, 8, 9, 4]
# they_numbers = [5, 7, 6, 8, 9, 4, 5, 4]
#
# matrix_on_my_numbers = matrix(my_numbers)
# my_numbers.extend([10, 12, 15])
# result = map(matrix_on_my_numbers, they_numbers)
# pprint(list(result))

#===================================================================================================
#-----------------------Создание объекта который можно вызвать----------------------------------------
class Multiplier:
    def __init__(self,n):
        self.n = n

    def __call__(self, x):
        # Если есть этот метод у класса то его объект можно вызвать как функцию
        return x * self.n

my_numbers = [2, 4, 5, 6, 7, 8, 9]
by_100500 = Multiplier(n=100500)

result = by_100500(x=42)
print(result)

result = map(by_100500,my_numbers)
print(list(result))
