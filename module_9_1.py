def apply_all_func(int_list, *functions):
    result = {}
    for all_func in functions:
        result[all_func.__name__] = all_func(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
