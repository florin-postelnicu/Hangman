from abc import ABC


class Animal(ABC):
    def make_sound(self):
        print("I lost my tongue")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")




class Chicken(Animal):
    def get_real(self):
        print(self, 'I am real')


def animal_sound(animals: list[Animal]):
    for animal in animals:
        animal.make_sound()


dog = Dog()  # dog is overriding the method in parent class (polymorphism)
cat = Cat()  # cat is overriding the method in parent class (polymorphism)
rooster = Chicken()  # rooster will inherit the animal_sound from the parent class
animal_sound([dog, cat, rooster])

no_real_thing([dog, cat, rooster])
