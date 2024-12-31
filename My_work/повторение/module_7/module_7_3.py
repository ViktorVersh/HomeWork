"""
Задача: Найдёт везде"
"""


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
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
        find_words = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_words[key] = value.index(word.lower()) + 1
        return find_words

    def count(self, word):
        count_words = {}
        for key, value in self. get_all_words().items():
            count = 0
            for i in value:
                if word.lower() == i:
                    count += 1
                count_words[key] = count
            return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('if')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего