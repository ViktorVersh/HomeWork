import shutil

# Исходный файл, который нужно копировать
source_file = './image/original.jpg'

# Диапазон номеров для новых файлов
for i in range(1, 401):
    # Формируем имя нового файла
    new_filename = f'./image/img_{i}.jpg'

    # Копируем исходный файл под новым именем
    shutil.copy(source_file, new_filename)
