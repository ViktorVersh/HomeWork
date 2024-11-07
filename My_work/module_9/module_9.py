"""
Вызов разом.
"""


def apply_all_func(int_list, *functions):  # Принимает список чисел и список функций
    result = {}  # Создаем словарь
    for i in functions:
        result[i.__name__] = i(int_list)  # Создаем ключ - значение
    return result  # Возвращаем словарь


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
