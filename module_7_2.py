def custom_write(file_name, strings):
    str_count = 0
    strings_positions = {}
    file = open(file_name, 'r+', encoding= 'utf-8')
    for strings in info:
        str_count += 1
        strings_positions.update({(str_count, file.tell()): strings})
        file.write(f'{strings}\n')
    file.close()
    return strings_positions

info = ['Text for tell.','Используйте кодировку utf-8.','Because there are 2 languages!','Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)