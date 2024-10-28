from sortfunc import *

from My_work.module_4.sortfunc import buble_sort, selection_sort

data1 = list(map(int, input('Введите числа через пробел:').split()))
data2 = list(map(int, input('Введите числа через пробел:').split()))

buble_sort(data1)
selection_sort(data2)

print('пузырьковая сортировка', data1)
print('Сортировка выборкой', data2)

