# def nul_decorator(func):
#     return func()
#
#
# def greet():
#     return 'Hello'
#
# print(greet())
# greet = nul_decorator(greet)
# print(greet)

#=============================================================================================

# def nul_decorator(func):
#     def wrapper():
#         orig_result = func()
#         mod_result = orig_result.upper()
#         return mod_result
#     return wrapper
#
# @nul_decorator
# def greet():
#     return 'Hello!'
#
# print(greet())

#====================================================================================================
import time
import sys


def time_track(func):
    def surogate(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed = round((start_time - end_time), 4)
        print(f'Функция работала {elapsed} минут')
        return result
    return surogate


@time_track
def digits(*args):
    total = 1
    for i in args:
        total *= i ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100000)
result = digits(5648, 4782, 1234, 9548)
print(result)
