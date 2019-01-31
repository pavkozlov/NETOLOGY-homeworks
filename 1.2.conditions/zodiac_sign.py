month = input('Введите месяц: ').lower()
date = int(input('Введите число: '))

if month == 'март':
    if 21 <= date <= 31:
        print('Овен')
    if 1 <= date <= 20:
        print('Рыбы')

elif month == 'апрель':
    if 1 <= date <= 19:
        print('Овен')
    if 20 <= date <= 31:
        print('Телец')

elif month == 'май':
    if 21 <= date <= 31:
        print('Близнецы')
    if 1 <= date <= 20:
        print('Телец')

elif month == 'июнь':
    if 1 <= date <= 20:
        print('Близнецы')
    if 21 <= date <= 31:
        print('Рак')

elif month == 'июль':
    if 23 <= date <= 31:
        print('Лев')
    if 1 <= date <= 22:
        print('Рак')

elif month == 'август':
    if 1 <= date <= 22:
        print('Лев')
    if 23 <= date <= 31:
        print('Дева')

elif month == 'сентябрь':
    if 23 <= date <= 31:
        print('Весы')
    if 1 <= date <= 22:
        print('Дева')

elif month == 'октябрь':
    if 1 <= date <= 22:
        print('Весы')
    if 23 <= date <= 31:
        print('Скорпион')

elif month == 'ноябрь':
    if 22 <= date <= 31:
        print('Стрелец')
    if 1 <= date <= 21:
        print('Скорпион')

elif month == 'декабрь':
    if 1 <= date <= 21:
        print('Стрелец')
    if 22 <= date <= 31:
        print('Козерог')


elif month == 'январь':
    if 1 <= date <= 19:
        print('Козерог')
    if 20 <= date <= 31:
        print('Водолей')


elif month == 'февраль':
    if 1 <= date <= 18:
        print('Водолей')
    if 19 <= date <= 31:
        print('Рыбы')

else:
    print('Такой месяц не найден!')
