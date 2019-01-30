from contextlib import contextmanager
from datetime import datetime


@contextmanager
def return_time(file_path):
    try:
        print("\nНачало работы программы: ", datetime.now().time(), '\n')
        starting_time = str(datetime.now().time())[9:]
        file = open(file_path, encoding='UTF-8')
        yield file
    finally:
        file.close()
        print("\nКонец работы программы: ", datetime.now().time())
        finally_time = str(datetime.now().time())[9:]
        result = (int(finally_time) - int(starting_time)) / 1000000
        print("Программа отработала за {} секунды".format(result))


with return_time('cook_book.txt') as file:
    counter = 0
    symbols = 0
    max_len_line = 0
    min_len_line = len(file.readline())
    for lines in file:
        counter += 1
        symbols += len(lines)
        if len(lines) > max_len_line:
            max_len_line = len(lines)
        if len(lines) < min_len_line:
            min_len_line = len(lines)
        print('В {} строке {} символов'.format(counter, len(lines)))
    print('\nВсего в файле {} строк'.format(counter))
    print('Всего в файле {} символов'.format(symbols))
    print('В среднем, срока имеет длину {} символов'.format(round(symbols / counter, 2)))
    print('Строка максимальной длины равна {} символов'.format(max_len_line))
    print('Строка минимальной длины равна {} символов'.format(min_len_line))
