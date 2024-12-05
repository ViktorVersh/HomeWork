data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    """
    Функция подсчета содержимого переменной data_structure
    :param data_structure:
    :return: Возвращает сумму ысех чисел, сумму длин строк, ключей и т.д.
    """
    result_sum = 0
    for i in data_structure:
        if isinstance(i, int):
            result_sum += i
        elif isinstance(i, str):
            result_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            inter_sum = calculate_structure_sum(i)
            result_sum += inter_sum
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, str):
                    result_sum += len(key)
                if isinstance(key, int):
                    result_sum += key
                if isinstance(value, int):
                    result_sum += value
                if isinstance(value, str):
                    result_sum += len(value)
    return result_sum


result = calculate_structure_sum(data_structure)
print(result)
