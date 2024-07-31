calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string:str):
    len_string = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    count_calls()
    return len_string,string_upper,string_lower


def is_contains(string:str,list_to_search:list):
    count_calls()
    if string.lower() in [i.lower() for i in list_to_search]:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBAN']))  #Urban~urBAN
print(is_contains('cycle',['recycling','cyclic']))  #No matcher
print(calls)