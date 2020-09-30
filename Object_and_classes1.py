# ЗАДАЧА 1

class Animal:
    geolocation = 'Ферма Дядюшки Джо'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food    # кг. еды
        print(f'{self.name}: поел(а)')

class Bird(Animal):
    food = ("семена", "зерна")

    def collect_eggs(self, eggs):
        self.weight -= 0.08 * eggs    # кол-во яиц
        print(f'{self.name}: яйца собраны')

class Goose(Bird):
    voice = 'honk'

class Chicken(Bird):
    voice = 'cock-a-doodle-doo'

class Duck(Bird):
    voice = 'quack-quack'


class ClovenHoofed(Animal):
    food = ("трава", "сено")

    def milky(self, milk_volume):
        self.weight -= milk_volume  # литров молока
        print(f'{self.name}: животное подоили')

class Cow(ClovenHoofed):
    voice = 'moo'

class Sheep(ClovenHoofed):
    voice = 'baa'

    def cut_wool(self, wool):
        self.weight -= wool    # кг. шерсти
        print(f'{self.name}: пострижен')

class Goat(ClovenHoofed):
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
print(f'Общий вес животных на ферме: {num_} кг')

# Вывести название самого тяжелого животного.
max = 0
heavy_animal = ''
for animal in farm:
    if animal.weight > max:
        max = animal.weight
        heavy_animal = animal
print(f'Самое тяжелое животное на ферме: {heavy_animal.name}\n')

# Задание 2:
# Используя методы из родительского класса,
# вызывать их в цикле у списка всех животных.

for animal in farm:
    animal.feed(1)
    print(f'теперь его вес: {animal.weight} кг')
print()

birds_on_the_farm = [seriy, beliy, ko_ko, kukarekoo, kryakva]

for animal in birds_on_the_farm:
    animal.collect_eggs(5)
    print(f'теперь его вес: {animal.weight} кг')
print()

cloven_hoofed_on_the_farm = [manka, barashek, kudryaviy, roga, kopita]

for animal in cloven_hoofed_on_the_farm:
    animal.milky(2)
    print(f'теперь его вес: {animal.weight} кг')
