# #-----------------------------Код Данила-------------------------------
# data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
#                   ((), [{(2, 'Urban', ('Urban2', 35))}])]
#
# # print(data_structure, '\n')
# # Список [1, 2, 3]
# lis = sum(data_structure[0])  # Список [1, 2, 3],
#
# #{'a': 4, 'b': 5}
# tup_one = int(len(list(data_structure[1])))  # {'а': 4, 'b': 5}, перевод букв в цифры в список
# tup_two = data_structure[1]  # {'а': 4, 'b': 5}, перевод букв в цифры без ключей a b
# tup_three = sum(tup_two.values())  # {'а': 4, 'b': 5}, перевод ключей 4 5
#
#
# #(6, {'cube': 7, 'drum': 8}),
# top_six = data_structure[2][0]  # Цифра 6
# tup_two_one = data_structure[2][1]  # перевод букв в цифры в список
# tup_two_1 = sum(tup_two_one.values())  # ключи в кортеже {'cube': 7, 'drum': 8}
# tup_two_2 = list(tup_two_one) # перевод в список
# tup_two_3 = len(tup_two_2[0]) #cube
# tup_two_4 = len(tup_two_2[1]) #drum
# tup_sum = tup_two_3 + tup_two_4
#
# txt_hello = len(data_structure[3]) #'Hello' подсчет букв
#
# listen_start = []
# for  i in data_structure[4][1]:
#     listen_start += i
#     continue
# listen_one = 0
# # listen_one = listen_start.keys()
# for i in listen_start:
#     if isinstance(i, int):
#         listen_one = listen_one + i
#     elif isinstance(i, str):
#         listen_one += len(i)
#     if isinstance(i, (set, list, tuple)):
#         for j in i:
#             if isinstance(j, int):
#                 listen_one += j
#             elif isinstance(j, str):
#                 listen_one += len(j)
#         continue
#
#
# # def calculate_structure_sum(*args):
# #     for i in data_structure:
# #         return tup_one + lis + tup_three + top_six + tup_two_1 + tup_sum + txt_hello + listen_one
#
# # result = calculate_structure_sum(data_structure)
#
# result = tup_one + lis + tup_three + top_six + tup_two_1 + tup_sum + txt_hello + listen_one
# print(result)
#

#---------------------------------мой код--------------------------------------
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    result_sum = 0
    for i in data_structure:
        if isinstance(i, int):
            result_sum += i
        elif isinstance(i, str):
            result_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            inter_sum = calculate_structure_sum(i)
            result_sum += inter_sum
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, str):
                    result_sum += len(key)
                elif isinstance(key, int):
                    result_sum += key
                if isinstance(value, int):
                    result_sum += value
                elif isinstance(value, str):
                    result_sum += len(value)
    return result_sum


print(calculate_structure_sum(data_structure))

