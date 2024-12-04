def print_params(a=1, b='строка', c=True):
    print(f'{a} {b} {c}')


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [12, '1, 2, 3', [1, 2, 3, 4]]
value_dict = {'a': 2, 'b': [1, 3, 5], 'c': False}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = [123, [1, 2, 3]]
print_params(*value_list_2, 42)
