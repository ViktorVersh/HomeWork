class WordsFinder:


    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        """
        подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        """
        all_words = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                text = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(i, '')
                words_text = text.split()
                all_words[f] = words_text
        return all_words

    def find(self, word):
        """
        Метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла.
        """
        res = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                res[key] = value.index(word.lower()) + 1
        return res


    def count(self, word):
        """
        метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
        количество слова word в списке слов этого файла.
        """
        res = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in value:
                if word.lower() == i:
                    count += 1
                res[key] = count
        return res

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
