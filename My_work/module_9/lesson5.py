#______________________________Пример 1 библиотека itertools_________________________________
# import sys
# from itertools import repeat
#
#
# ex_iterator = repeat('4', 100_000)
# print(ex_iterator)
# print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')
#
# ex_iter = '4' * 100_000
# print(f'размер списка - {sys.getsizeof(ex_iter)}')

#===================================================================================================
# class Iter:
#     def __init__(self):
#         self.first = 'Первый элемент'
#         self.second = 'Второй элемент'
#         self.third = 'Третий элемент'
#         self.i = 0
#
#     def __iter__(self):
#         # обнуляем счетчик
#         self.i = 0
#         # возвращаем ссылку на самого себя, тк сам объект должен быть итератором
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             print('Подсчет закончен')
#             raise StopIteration()
#
# obj = Iter()
# print(obj)
#
# # for value in obj:
# #     print(value)
# try:
#     while True:
#         value = obj.__next__()
#         print(value)
#
# except StopIteration:
#     pass

#=======================================================================================================
#________________________________пример функции «fibonacci»___________________________________
# def fibonacci(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
# for value in fibonacci(n=10):
#     print(value)
#=====================================================================================================
#________________________________пример функции «fibonacci» с итератором___________________________________
class Fibonacci:
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b, = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            self.a, self.b = self.b, self.a + self.b
            if self.i > self.n:
                raise StopIteration
        return self.a


fib_iterator = Fibonacci(20)
for value in fib_iterator:
    print(value)
