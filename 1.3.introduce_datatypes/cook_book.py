cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]

print("Имеются рецепты: ", end='')
for i in cook_book:
    print(i[0], end=', ')
selected_dish = input("\nЧто готовим?\n").lower()
person = int(input("Сколько человек?\n"))

for dishes in cook_book:
    if selected_dish == dishes[0]:
        print(dishes[0].capitalize())
        for ingredients in dishes[1]:
            print('{}, {}гр.'.format(ingredients[0], ingredients[1] * person))