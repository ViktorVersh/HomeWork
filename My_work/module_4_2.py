def test_function():
    def inner_function():
        print('я в области видимости test_function')

    inner_function()


test_function()

"""
вызов inner_function() вне функции test_function() - Выдает ошибку:
name 'inner_function' is not defined. Did you mean: 'test_function'?
имя 'inner_function' не определено. Вы имели в виду: 'test_function'?
"""
