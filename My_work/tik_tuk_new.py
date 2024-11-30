def check_winner(area):
    # Проверяем строки
    for i in range(3):
        if area[i][0] == area[i][1] == area[i][2] != '*':
            return area[i][0]

    # Проверяем столбцы
    for j in range(3):
        if area[0][j] == area[1][j] == area[2][j] != '*':
            return area[0][j]

    # Проверяем диагонали
    if area[0][0] == area[1][1] == area[2][2] != '*':
        return area[0][0]
    if area[2][0] == area[1][1] == area[0][2] != '*':
        return area[2][0]

    return '*'


def draw_area(area):
    for i in area:
        print(*i)
    print()


def is_full(area):
    for row in area:
        if '*' in row:
            return False
    return True


def main():
    area = [['*'] * 3 for _ in range(3)]
    print('Добро пожаловать в крестики-нолики')
    print('----------------------------------')

    while True:
        for i in range(1, 10):
            print(f'Ход: {i}')
            if i % 2 == 0:
                turn_char = '0'
                print('Ходят нолики')
            else:
                turn_char = 'X'
                print('Ходят крестики')

            draw_area(area)

            while True:
                try:
                    row = int(input('Введите номер строки: 1,2,3  ')) - 1
                    column = int(input('Введите номер столбца: 1,2,3  ')) - 1
                    if area[row][column] == '*':
                        area[row][column] = turn_char
                        break
                    else:
                        print('Ячейка уже занята, попробуйте снова.')
                except (ValueError, IndexError):
                    print('Некорректный ввод, попробуйте снова.')

            winner = check_winner(area)
            if winner != '*':
                print(f'Победа {winner}')
                draw_area(area)
                return

        if is_full(area):
            print('Ничья')
            draw_area(area)
            return


if __name__ == "__main__":
    main()
