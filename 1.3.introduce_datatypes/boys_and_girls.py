boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()

if len(boys) != len(girls):
    print("Кто-то может остаться без пары!")
else:
    total_list = zip(boys, girls)
    print('Идеальные пары:')
    for people in list(total_list):
        boy, girl = people
        print(boy, 'и', girl)
