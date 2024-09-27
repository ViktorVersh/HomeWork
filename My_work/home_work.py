def sum_numbers_and_string_lengths(*data_structure):
    total_sum = 0
    # total_length = 0
    for item in data_structure:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):
            # inner_sum, inner_length = sum_numbers_and_string_lengths(item)
            inner_sum = sum_numbers_and_string_lengths(item)
            total_sum += inner_sum
            # total_length += inner_length
        elif isinstance(item, dict):
            for key, value in item.items():
                # Суммируем ключи словаря
                if isinstance(key, str):
                    total_sum += len(key)
                elif isinstance(key, int):
                    total_sum += key
                # Суммируем значения словаря
                if isinstance(value, int):
                    total_sum += value
                elif isinstance(value, str):
                    total_sum += len(value)
                elif isinstance(value, (list, tuple, set)):
                    # inner_sum, inner_length = sum_numbers_and_string_lengths(value)
                    inner_sum = sum_numbers_and_string_lengths(value)
                    total_sum += inner_sum
                    # total_length += inner_length
                elif isinstance(value, dict):
                    # inner_sum, inner_length = sum_numbers_and_string_lengths([value])
                    inner_sum = sum_numbers_and_string_lengths([value])
                    total_sum += inner_sum
                    # total_length += inner_length
    return total_sum


# Заданные входные данные

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

# Вызов функции

total_sum = sum_numbers_and_string_lengths(data_structure)

print("Сумма всех чисел:", total_sum)

# print("Сумма длин всех строк:", total_length)

'''

Описание работы кода:

1. Функция `sum_numbers_and_string_lengths` принимает на вход структуру данных.

2. Внутри функции инициализируются переменные `total_sum` и `total_length`, которые будут хранить сумму чисел
и общую длину строк соответственно.

3. Код обходит каждый элемент в предоставленной структуре данных. В зависимости от типа элемента:
- Если это число(int), оно добавляется к `total_sum`.
- Если это строка(str), ее длина добавляется к `total_length`.
- Если это коллекция(список, кортеж, множество), функция вызывается рекурсивно.
- Если это словарь, ключи и значения обрабатываются индивидуально.

4. В конце функция возвращает общую сумму чисел и общую длину строк.

После выполнения кода вы получите сумму всех чисел и сумму длины всех строк, содержащихся в указанной структуре данных.
'''
