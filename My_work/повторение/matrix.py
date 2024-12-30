def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(value)
        matrix.append(a)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(5, 5, 42)
result3 = get_matrix(4, 3, 13)

for i in result1:
    print(i)
print()

for i in result2:
    print(i)
print()

for i in result3:
    print(i)
