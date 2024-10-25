from pprint import pprint

name = 'module_txt.txt'  # просто текстовый файл
file = open(name, 'r', encoding='UTF-8')  # r = read, w = write, a = append
print(file)
pprint(file.read())
file.close()

name = 'module_txt2.txt'
file = open(name, 'w', encoding='UTF-8')
file.write('Здравствуйте!!!\n Меня зовут Виктор\n Мне 57 лет \n Я учусь в университете Urban\n')
file.close()

name = 'module_txt2.txt'
file = open(name, 'a', encoding='UTF-8')
file.write('\nHello, world!')
file.close()

name = 'module_txt2.txt'
file = open(name, 'r', encoding='UTF-8')
pprint(file.read())
file.close()

name = 'module_txt2.txt'
file = open(name, 'a', encoding='UTF-8')
print(file.seek(30))
file.write('\nСегодня ясный солнечный день\n')
file.close()

name = 'module_txt2.txt'
file = open(name, 'r', encoding='UTF-8')
print(file.tell())
print(file.writable())
print(file.readable())
print(file.seekable())
file.close()