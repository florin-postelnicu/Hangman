'''
If the method exists in subclass, then it will override the method yin the parent class
Polymorphism

If the method doesn't exist in subclass, then the instance from the subclass
will inherit the method from the parent class
Inheritance
'''

class Animal():
    def __init__(self):
        pass
    def claim_animal(self):
        print("Hey, I am an animal!")

    def noise_animal(self):
        print( " I usually talk louder!")

class Cat(Animal):
    def __init__(self):
        pass
    def claim_animal(self):
        print("I am a cat!")

    def noise_animal(self):
        print("Meow!")

class Dog(Animal):
    def claim_animal(self):
        print("I am a dog")


class Chicken(Animal):
    def __init__(self):
        pass

    def noise_animal(self):
       print("Cocorico!")

cat = Cat()
dog = Dog()
chicken = Chicken()

list_animals = [cat, dog, chicken]
print( "Who am I?")
for animal in list_animals:
    print(animal)
    animal.claim_animal()

print ( " The Voice")
for animal in list_animals:
    print(animal)
    animal.noise_animal()
