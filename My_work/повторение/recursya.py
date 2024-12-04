def summ_all(n):

    if n == 1:
        return 1
    else:
        return n + summ_all(n - 1)


print(summ_all(10))


def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
