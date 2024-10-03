nums = [5, 6, 3, 2, 1, 4, 10, 12, 11, 7, 16, 8, 13, 9, 14, 15]


def buble_sort(ls):  # - пузырьковая сортировка "большая О=n^2"
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


buble_sort(nums)
print(nums)


def section_sort(ls):  # сортировка выборкой
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
                ls[i], ls[lowest] = ls[lowest], ls[i]


section_sort(nums)
print(nums)
