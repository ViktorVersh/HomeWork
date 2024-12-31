"""
Задача: Найдёт везде"
"""


class WordsFinder:
    """
    Класс для поиска слов в файлах
    """
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        """
        Возвращает слова из всех файлов в виде словаря имя файла: список слов
        :return:
        """
        all_words = {}
        for i in self.file_names:
            with open (i, 'r', encoding='utf-8') as f:
                line = f.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(j, '')
                    line1 = line.split()
                all_words[i] = line1
        return all_words

    def find(self, word):
        """
        Находит первое вхождение слова в тексте и возвращает номер слова в списке
        :param word:
        :return:
        """
        find_words = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_words[key] = value.index(word.lower()) + 1
        return find_words

    def count(self, word):
        """
        Считает количество вхождений слова в тексте
        :param word:
        :return:
        """
        count_words = {}
        for key, value in self. get_all_words().items():
            count = 0
            for i in value:
                if word.lower() == i:
                    count += 1
                count_words[key] = count
        return count_words


#  ===========Пример выполнения с одним файлом===========
#
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('if')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#  ===========Пример выполнения с несколькими файлами===========

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))