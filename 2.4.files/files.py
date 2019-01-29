units_list = ['ingredient_name', 'quantity', 'measure']
cook_book = {}
with open('cook_book.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        name = line.strip()
        count = f.readline().strip()
        for i in range(int(count)):
            ingredient_list = dict(zip(units_list, f.readline().strip().split('|')))
            if cook_book.get(name) is not None:
                cook_book[name].append(ingredient_list)
            else:
                cook_book[name] = [ingredient_list]
        f.readline()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in cook_book:
        if dish in dishes:
            for ingredient in cook_book[dish]:
                result[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': int(ingredient['quantity']) * person_count}
    for ingredients in result:
        print(ingredients, result[ingredients])
    return result


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 20)
