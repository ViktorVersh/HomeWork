def sum_numbers_and_string_lengths(data_structure):
    itog_sum = 0
    for i in data_structure:
        if isinstance(i, int):
            itog_sum += i
        elif isinstance(i, str):
            itog_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            inner_sum = sum_numbers_and_string_lengths(i)
            itog_sum += inner_sum
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, str):
                    itog_sum += len(key)
                elif isinstance(key, int):
                    itog_sum += key
                if isinstance(value, int):
                    itog_sum += value
                elif isinstance(value, str):
                    itog_sum += len(value)
                elif isinstance(value, (list, tuple, set)):
                    inner_sum = sum_numbers_and_string_lengths(value)
                    itog_sum += inner_sum
                elif isinstance(value, dict):
                    inner_sum = sum_numbers_and_string_lengths([value])
                    itog_sum += inner_sum
    return itog_sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


value_sum = sum_numbers_and_string_lengths(data_structure)
print(value_sum)
