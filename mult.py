for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j}\t', end='')
    print()

print()
for i in range(1, 11):
    for j in range(1, 11):
        print('%s * %s = %s\t' % (i, j, i*j), end='')
    print()

print()
for i in range(1, 11):
    for j in range(1, 11):
        print('{} * {} = {}\t'.format(i, j, i*j), end='')
    print()
