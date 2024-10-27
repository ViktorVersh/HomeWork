class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}  # имя файла и слова
        for file_name in self.file_names:  # проходим по всем файлам
            with open(self.file_names[0], encoding='utf-8') as file:  # открываем файл
                words = []  # список слов
                for line in file:  # проходим по всему тексту
                    line = line.lower()  # преобразуем строку в нижний регистр
                    mask_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']  # знаки препинания для замены
                    for m_punc in mask_punctuation:  # цикл для поиска каждого знака препинания
                        line = line.replace(m_punc, ' ')  # заменяем знак препинания на пробел
                    words.extend(line.split())  # добавляем слова в список
            all_words[file_name] = words  # добавляем слова в словарь
        return all_words  # возвращаем словарь

    def find(self, word):
        find_w = {}  # имя файла и индекс слова
        for key, value in self.get_all_words().items():
            if word.lower() in value:  # если слово есть в тексте
                find_w[key] = value.index(word.lower()) + 1  # +1 для того, чтобы найти индекс
            return find_w  # возвращаем словарь

    def count(self, word):
        count_w = {}  # имя файла и количество слов
        for value, key in self.get_all_words().items():
            count_word = key.count(word.lower())  # считаем количество слов
            count_w[value] = count_word  # добавляем количество слов в словарь
        return count_w  # возвращаем словарь


finder2 = WordsFinder('test_file.txt')
get_all_words = finder2.get_all_words()
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
