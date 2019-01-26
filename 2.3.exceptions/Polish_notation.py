nums = input('Введите выражение: ').split(' ')

symbols = ['+', '-', '*', '/']

assert nums[0] in symbols, 'Введёный знак не + - / *'

try:
    if nums[0] == '+':
        print(int(nums[1]) + int(nums[2]))
    elif nums[0] == '-':
        print(int(nums[1]) - int(nums[2]))
    elif nums[0] == '*':
        print(int(nums[1]) * int(nums[2]))
    elif nums[0] == '/':
        try:
            print(int(nums[1]) / int(nums[2]))
        except ZeroDivisionError:
            print('Деление на ноль невозможно')
        except TypeError:
            print('Обнаружена строка. Конфликт типов!')
except IndexError:
    print('Необходимо ввести 2 числа!')
