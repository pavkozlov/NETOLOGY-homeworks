class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.satiety = 5

    def feed(self):
        self.satiety += 1


class Birds(Animal):
    eggs = 9

    def collect_eggs(self):
        if self.eggs:
            self.eggs -= 1
        else:
            print("Яиц пока нет")


class Goose(Birds):
    def say_hello(self):
        print("Га Га Га")


class Duck(Birds):
    def say_hello(self):
        print("Кря Кря Кря")


class Hen(Birds):
    def say_hello(self):
        print("Ко Ко Ко")


class Cow(Animal):
    milk = 3

    def collect_milk(self):
        if self.milk:
            self.milk -= 1
        else:
            print("Молоко кончилось")

    def say_hello(self):
        print("Муу Муу")


class Sheep(Animal):
    wool = True

    def collect_wool(self):
        if self.wool:
            self.wool = False
        else:
            print("Шерсть не выросла!")

    def say_hello(self):
        print("Бее Бее")


class Goat(Animal):
    milk = 3

    def collect_milk(self):
        if self.milk:
            self.milk -= 1
        else:
            print("Молоко кончилось")

    def say_hello(self):
        print("Мее Мее")


white = Goose("Белый", 500)
grey = Goose("Серый", 300)

coco = Hen("Ко-Ко", 100)
kukareku = Hen("Кукареку", 200)

kryakva = Duck("Кряква", 900)

manya = Cow("Манька", 12000000)

barashek = Sheep("Барашек", 11000000)
kudryavi = Sheep("Курдявый", 9000000)

roga = Goat("Рога", 5000000)
kopita = Goat("Копыта", 3400000)

uncle_joes_farm = [white, grey, coco, kukareku, kryakva, manya, barashek, kudryavi, roga, kopita]

total_weight = 0
max_weight = 0

for animal in uncle_joes_farm:
    print("{} приветствует нас: ".format(animal.name), end='')
    animal.say_hello()
    total_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
    animal.feed()
    if type(animal) == Goose or type(animal) == Duck or type(animal) == Hen:
        animal.collect_eggs()
    if type(animal) == Cow or type(animal) == type(animal) == Goat:
        animal.collect_milk()
    if type(animal) == Sheep:
        animal.collect_wool()

print("Максимальный вес животного: ", max_weight)
print("Общий вес: ", total_weight)
