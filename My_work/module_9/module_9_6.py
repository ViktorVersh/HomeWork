"""
Задача: Напишите функцию-генератор
"""


def all_variants(text):
    len_text = len(text)  # создаем переменную с длиной строки
    for i in range(1, len_text + 1):  # Проходимся циклом по всей длине строки, включая последний символ
        for j in range(len_text - i + 1):  # проходим циклом по строке с позиции 0 до i включительно
            # ключевое слово yield превращает функцию в генератор
            yield text[j: j + i]  # возвращаем подстроку, начинающуюся с индекса j и имеющую длину i


a = all_variants("abc")
for i in a:
    print(i)
