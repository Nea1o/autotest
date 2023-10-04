from main_package.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно! пустая строка')

if capitalize('2') != '2':
    raise Exception('Функция работает неверно! c 1 символом')

if capitalize(' ') != ' ':
    raise Exception('Функция работает неверно! c пробелом')