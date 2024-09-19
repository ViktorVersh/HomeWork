def stone_pass(num):
    crunch_num = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                crunch_num += str(i) + str(j)
    return crunch_num


print('Введите число')
print(stone_pass(int(input())))
