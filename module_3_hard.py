def calculate_structure_sum(data_structure):
    total_sum = 0
    string_sum = 0

    def recurse(data):
        nonlocal total_sum, string_sum
        if isinstance(data, (list, tuple, set)):
            for item in data:
                recurse(item)
        elif isinstance(data, dict):
            for value in data.values():
                recurse(value)
            for key in data.keys():
                recurse(key)
        elif isinstance(data, int):
            total_sum += data
        elif isinstance(data, str):
            string_sum += len(data)

    recurse(data_structure)
    return total_sum +string_sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)