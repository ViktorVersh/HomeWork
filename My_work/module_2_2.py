first = input("Введите первое целое число: ")
second = input("Введите второе целое число: ")
third = input("Введите третье целое число: ")
if first == '' or second == '' or third == '':
    print('Вы неправильно ввели число')
elif first == second == third:
    print('Совпадающих цифр 3')
elif first != second and first != third and second != third:
    print("Совпадающих чисел 0")
else:
    print("Совпадающих чисел 2")
