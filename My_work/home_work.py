data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def sum_numbers_and_string_lengths(data_structure):
    result_sum = 0
    for i in data_structure:
        if isinstance(i, int):
            result_sum += i
        elif isinstance(i, str):
            result_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            inter_sum = sum_numbers_and_string_lengths(i)
            result_sum += inter_sum
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, str):
                    result_sum += len(key)
                elif isinstance(key, int):
                    result_sum += key
                if isinstance(value, int):
                    result_sum += value
                elif isinstance(value, str):
                    result_sum += len(value)
                elif isinstance(value, (list, tuple, set)):
                    inter_sum = sum_numbers_and_string_lengths(value)
                    result_sum += inter_sum
                elif isinstance(value, dict):
                    inter_sum = sum_numbers_and_string_lengths([value])
                    result_sum += inter_sum
    return result_sum


print(sum_numbers_and_string_lengths(data_structure))
