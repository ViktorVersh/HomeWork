import numpy as np


def create_matrix(n, m):
    """Создаем двумерную матрицу размера n x m со случайными целыми числами от 100 до 1000."""
    return np.random.randint(100, 1001, size=(n, m))


def sum_rows(matrix):
    """Вычисляем сумму элементов каждой строки матрицы."""
    return np.sum(matrix, axis=1)


def sum_columns(matrix):
    """Вычисляем сумму элементов каждого столбца матрицы."""
    return np.sum(matrix, axis=0)


def max_element(matrix):
    """Находим максимальный элемент матрицы."""
    return np.max(matrix)


def min_element(matrix):
    """Находим минимальный элемент матрицы."""
    return np.min(matrix)


def sum_diagonals(matrix):
    """Вычисляем сумму элементов обеих диагоналей матрицы."""
    main_diagonal = np.trace(matrix)
    anti_diagonal = np.trace(np.fliplr(matrix))
    return main_diagonal + anti_diagonal



# Создание матрицы
matrix = create_matrix(5, 5)
print("Матрица:")
print(matrix)

# Вывод результатов
print(f"Суммы элементов по строкам: {sum_rows(matrix)}")
print(f"Суммы элементов по столбцам: {sum_columns(matrix)}")
print(f"Максимальный элемент: {max_element(matrix)}")
print(f"Минимальный элемент: {min_element(matrix)}")
print(f"Сумма элементов диагоналей: {sum_diagonals(matrix)}")
