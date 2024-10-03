# a_str = []
#
#
def test_function():
    # global a_str
    # a_str = ' основная функция'
    # print(a_str)
    # a = []

    def inner_function():
        print('Я в области видимости функции test_function')
        # nonlocal a
        # a = ' я в области видимости test_function '

    inner_function()
    # print(a)


test_function()

"""
вызов inner_function() вне функции test_function() - Выдает ошибку:
name 'inner_function' is not defined. Did you mean: 'test_function'?
имя 'inner_function' не определено. Вы имели в виду: 'test_function'?
"""
