immutable_var= 1, 2, 3, 4, 5, "string", True
print('immutable tuple: ', immutable_var)
# immutable_var [1]=35      при попытке изменении элементов кортежа
# type(immutable_var)       выдается ошибка - 'tuple' object does not support item assignment
#                           потому-что элементы кортежа неизменяемы - это отличие кортежа от списка
mutable_list=[1, 2, 3, 4, 5, "string", True]
print('mutable list: ', mutable_list)
mutable_list[1]=35
print('mutable list new:', mutable_list)    # список можно изменять