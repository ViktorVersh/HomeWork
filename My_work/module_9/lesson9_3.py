#-------------------------------Ленивые вычисления-------------------------------------
# Производятся только тогда когда нам нужно (при необходимости)
# Это делают генераторы

# my_num = [2, 3, 5, 6, 1, 4, 9, 7, 8]
#
# result = (x**100 for x in my_num)
# print(result)
#
# for i in result:
#     print(i)
#
# print('Ещё разок')
#
# for i in result:
#     print(i)

import time

# start_time = time.time()
#
# my_num = [2, 3, 5, 6, 1, 4, 9, 7, 8]
# result = (x**3000 for x in my_num) # Генераторная сборка
# print(result)
# for i in result:
#     print(i)
#
# finish_time = time.time()
# print(f'Затрачено времени в милисекундах {(finish_time - start_time)*1000}')

#
# start_time = time.time()
#
# my_num = [2, 3, 5, 6, 1, 4, 9, 7, 8]
# result = [x**3000 for x in my_num] # Строковая сборка
# print(result)
# for i in result:
#     print(i)
#
# finish_time = time.time()
# print(f'Затрачено времени в милисекундах {(finish_time - start_time)*1000}')

# Ленивые вычисления в строенных функциях map, open, range, zip
list_1 = [1, 3, 2, 4, 5, 6]
list_2 = [3, 7, 8, 9, 6, 2]

ra = range(10, 30)
ma = map(str, list_1)
zi = zip(list_1, list_2)

print(ra, ma, zi)
print(list(ra))
print(list(ma))
print(list(zi))
