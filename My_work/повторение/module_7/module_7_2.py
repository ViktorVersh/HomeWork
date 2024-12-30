def custom_write(file_name, strings):
    with (open(file_name, 'w', encoding='utf-8') as file):
        string_position = {}
        for i in range(len(strings)):
            for j in strings:
                tell = file.tell()
                file.write(j + '\n')
                string_position[i + 1, tell] = j
                i += 1
            return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
