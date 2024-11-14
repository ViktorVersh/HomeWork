"""
Декораторы 1.2
"""
import time
import sys


def fun_gen_dec(precision):
    def dec(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)

            end_time = time.time()
            elapsed = round((end_time - start_time), precision)
            print(f'Функция работала {elapsed} минут')
            return result

        return wrapper

    return dec


@fun_gen_dec(precision=10)
def digits(*args):
    total = 1
    for i in args:
        total *= i ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10 ** 5)

# time_track_precision_6 = fun_gen_dec(precision=2)
# digits = time_track_precision_6(digits)
result = digits(5648, 4782, 1234, 9548)
print(f'Длина строки составила {result} символов')
