"""
Консольная игра угадай число
"""
import random
print('*' * 5, 'Угадай число', '*' * 5)
print("Компьютер случайно выберет число от 1 до 10")
print('*' * 3, "Вам нужно угадать это число", '*' * 3)
print('Для выхода из игры нажмите 0')
answer = 1
score = 0
i = 0
while answer:
    try:
        if answer == 0:
            break
        rand_num = random.randint(1, 10)
        answer = int(input('Введите число от 1 до 10: '))
        if answer == rand_num:
            print('Вы угадали')
            score += 1
            print('Ваш счет: ', score)
        else:
            print('Вы не угадали')
        i += 1
        print('Количество попыток: ', i)
        print("Общий счет: ", score, "из", i)
    except ValueError:
        print('Ошибка: Введите число от 1 до 10: ')
print('Игра окончена')
