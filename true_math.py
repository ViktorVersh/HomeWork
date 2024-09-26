from math import inf


def divide(first, second):
    j = 0
    if second == 0:
        return inf
    else:
        j = first / second
    return j


# result = divide(56, 8)
# print(result)
# result_1 = divide(54, 0)
# print(result_1)
