# -----------------------Списковый сборки--------------------------------

# _____________Объединение функций map и filter-----------------------------

# def by_3(x):
#     return x * 3
#
#
# def is_odd(x):
#     return x % 2
#
# my_numbers = [2, 3, 5, 6, 7, 1, 9, 8]
# result = map(by_3, filter(is_odd, my_numbers))
# print(list(result))

#-------------------Аналог map--------------------------------
# my_numbers = [2, 3, 5, 6, 7, 1, 9, 8]
# result = [x * 3 for x in my_numbers]
# print(result)
#
# numbers_my = [2, 4, 5, 7, 9, 8, 2, 1]
# result1 = {x * 5 for x in numbers_my} # создаем множество
# print(result1)
#
# number_my = [2, 4, 5, 7, 9, 8, 2, 1]
# result2 = {x: x * 5 for x in number_my} # создаем словарь
# print(result2)

#---------------------------Генерация списков с фильтрацией-------------------------------------

# my_numbers = [2, 3, 5, 6, 7, 1, 9, 8]
# result = [x * 3 for x in my_numbers if x % 2]
# print(result)

#----------------------------Изменение операций над объектами-----------------------------------

# my_numbers = [2, 3, 5, 6, 7, 1, 9, 8]
# result = [x * 3 if x > 5 else x * 10 for x in my_numbers]
# print(result)
#
# numbers_my = ['A', 1, 3, 'B', 5, 8, 'C', 4, 'D']
# result1 = [x if type(x) == str else x * 5 for x in numbers_my]
# print(result1)

#---------------------------Генерация для двух элементов---------------------------
my_numbers = [2, 3, 5, 6, 7, 1, 9, 8]
my_number = [2, 4, 5, 7, 9, 8, 2, 1]

result = [x * y for x in my_numbers for y in my_number]
print(result)

result1 = [x * y for x in my_numbers for y in my_number if x > 3]
print(result1)

result2 = [x * y for x in my_numbers for y in my_number if y % 2]
print(result2)

result3 = [x * y for x in my_numbers for y in my_number if x // 2 and y // 3]
print(result3)

