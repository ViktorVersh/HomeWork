calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    print(string)
    return


def is_contains(list_, list_to_search):
    count_calls()
    a = str(list_)
    b = str(list_to_search)
    if a.lower() in b.lower():
        print(True)
    else:
        print(False)
    return


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])  # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic'])  # No matches
print(calls)
