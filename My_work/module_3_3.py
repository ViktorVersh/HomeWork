def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params(a=1, b='строка',c=True)
print_params(a=1)
print_params(a=1,b='строка')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [3, '1, 2, 3', ["ручей", "река", "озеро" ]]
values_dict = {'a': 25, 'b': 'world', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [32.23, 'новости']

print_params(*values_list_2, 42)