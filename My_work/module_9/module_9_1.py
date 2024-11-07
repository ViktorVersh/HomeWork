"""
Задача "Вызов разом"
"""


def apply_all_func(int_list, *functions):  # функция принимает список чисел и список функций
    result = {}  # словарь: ключ - название вызванной функции, а значением - её результат работы со списком int_list
    for i in functions:  # перебираем все функции
        result[i.__name__] = i(int_list)  # создаём ключ-значение
    return result  # возвращаем словарь


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
