# ЗАДАЧА 1
class Animal:
    geolocation = 'Ферма Дядюшки Джо'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food    # кг. еды
        print('Животное поело')

class Bird(Animal):
    food = ("семена", "зерна")

    def collect_eggs(self, eggs):
        self.weight -= 0.08 * eggs    # кол-во яиц
        print('Нужное количество яиц собрано')

class Goose(Bird):
    voice = 'honk'

class Chicken(Bird):
    voice = 'cock-a-doodle-doo'

class Duck(Bird):
    voice = 'quack-quack'


class Cloven_hoofed(Animal):
    food = ("трава", "сено")

    def milky(self, milk_volume):
        if isinstance(self, Sheep):
            print('Дядюшка Джо не доит овец')
        else:
            self.weight -= milk_volume  # литров молока
            print('Животное подоили')

class Cow(Cloven_hoofed):
    voice = 'moo'

class Sheep(Cloven_hoofed):
    voice = 'baa'

    def cut_wool(self, wool):
        self.weight -= wool    # кг. шерсти
        print('Шерсть пострижена')

class Goat(Cloven_hoofed):
    voice = 'mee'

seriy = Goose('Серый', 9)
beliy = Goose('Белый', 10)
ko_ko = Chicken('Ко-Ко', 6)
kukarekoo = Chicken('Кукареку', 5)
kryakva = Duck('Кряква', 8)
manka = Cow('Манька', 400)
barashek = Sheep('Барашек', 100)
kudryaviy = Sheep('Кудрявый', 90)
roga = Goat('Рога', 50)
kopita = Goat('Копыта', 60)


farm = (seriy, beliy, ko_ko, kukarekoo, kryakva,
        manka, barashek, kudryaviy, roga, kopita)

# Необходимо посчитать общий вес всех животных(экземпляров класса)
num_ = 0
for animals in farm:
    num_ += animals.weight
print(f'Общий вес животных на ферме: {num_}')

# Вывести название самого тяжелого животного.
max = 0
heavy_animal = ''
for animal in farm:
    if animal.weight > max:
        max = animal.weight
        heavy_animal = animal
print(f'Самое тяжелое животное на ферме: {heavy_animal.name}')

# Задание со второго урока:
# Используя методы из родительского класса,
# вызывать их в цикле у списка всех животных.

for animal in farm:
    animal.feed(1)
for animal in farm:
    print(animal.weight)

birds_on_the_farm = [seriy, beliy, ko_ko, kukarekoo, kryakva]

for animal in birds_on_the_farm:
    animal.collect_eggs(5)
for animal in birds_on_the_farm:
    print(animal.weight)

Cloven_hoofed_on_the_farm = [manka, barashek, kudryaviy, roga, kopita]

for animal in Cloven_hoofed_on_the_farm:
    animal.milky(2)
for animal in Cloven_hoofed_on_the_farm:
    print(animal.weight)
