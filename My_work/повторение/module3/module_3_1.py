calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    string_tuple = (len(string), string.upper(), string.lower())
    count_calls()
    return string_tuple


def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in str(list_to_search).lower():
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
