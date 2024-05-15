"""
Создайте класс "Животное", который содержит информацию о виде и возрасте животного.
Создайте классы "Собака" и "Кошка", которые наследуются от класса "Животное" и содержат информацию о породе.
"""


class Animal:
    def __init__(self, vid, age):
        self.vid = vid
        self.age = age


class Dog(Animal):
    def __init__(self, vid, age, poroda):
        super().__init__(vid, age)
        self.poroda = poroda


class Cat(Animal):
    def __init__(self, vid, age, poroda):
        super().__init__(vid, age)
        self.poroda = poroda


dog = Dog('Собака', 5, 'Немецкая овчарка')
print(f'Вид: {dog.vid}.  Возраст: {dog.age}.  Порода: {dog.poroda}.')
cat = Cat('Кошка', 7, 'Русская голубая')
print(f'Вид: {cat.vid}.  Возраст: {cat.age}.  Порода: {cat.poroda}.')
