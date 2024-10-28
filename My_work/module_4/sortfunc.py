def buble_sort(ls):  # - пузырьковая сортировка "большая О=n^2"
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


def selection_sort(ls2):  # сортировка выборкой
    swap = True
    while swap:
        swap = False
        for i in range(len(ls2)):
            lowest = i
            for j in range(i + 1, len(ls2)):
                if ls2[j] < ls2[lowest]:
                    lowest = j
                    ls2[i], ls2[lowest] = ls2[lowest], ls2[i]
                    swap = True
