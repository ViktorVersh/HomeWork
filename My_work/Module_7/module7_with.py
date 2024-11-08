name = 'module_txt2.txt'
with open(name, encoding = 'utf-8') as file:
    for line in file:
        for char in line:
            print(char, end='')
    # print(line, end = '')
print(file.closed)
