"""
Генератор-это специальная функция, которая возвращает итератор.
"""

# ______________________________Создание простого генератора______________________________

# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
# obj = func_generator(10)
# print(obj)
#
# for i in obj:
#     print(i, end='  ')

# --------------------Создание функции Фибоначи---------------------------------------------
#
# def fibonacci(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
#
# re_fib = fibonacci(n=10)
# print(re_fib)
# for i in re_fib:
#     print(i, end='  ')
# print()
#
#
# def fibonacci_2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# re_fib2 = fibonacci_2(10)
# print(re_fib2)
#
# for i in re_fib2:
#     print(i, end='  ')

# ------------------------Пример 3-----------------------------------
# def fibonacci3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for i in fibonacci3():
#     print(i)
#     if i > 6**10:
#         break


# -----------------------------------Пример 4-------------------------------------------
import time

start = time.time()


def line_read_file(file_name):
    with open(file_name, 'r') as f:
        for i in f:
            yield i.strip()


for line in line_read_file('voyna-i-mir.txt'):
    print(line)

fin = time.time()
print((fin - start)*1000)
