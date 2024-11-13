"""
Задание: Декораторы в Python
"""


def is_prime(func):  # функция декоратор
    def wrapper(*args):
        result = func(*args)
        if result == 1 and result == 2:
            return False
        elif result == 3:
            print("Простое")
            return result
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                else:
                    print("Простое")
                return result
            return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(0, 0, 3, 5)
print(result)
