

class Animal(object):
    def __init__(self, animalName):
        print(animalName, 'is a animal.')
    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, mammalName):
        # super(Mammal, self).__init__(mammalName)
        super().__init__(mammalName)
        print(mammalName, 'is a warm-blooded.')
    # method overriding
    def make_sound(self):
        print("Sound: Some mammal sound")

class Terrrestrial(Animal):
    def __init__(self, terrestrialName):
        super().__init__(terrestrialName)
        print(terrestrialName, 'can walk.')
    # method overriding
    def make_sound(self):
        print("Sound: Walking sound")


class Cat(Mammal):
    def __init__(self):
        super().__init__('Cat')
        print('Im a Cat with four legs')
    # method overriding
    def make_sound(self):
        print("Sound: Miao, Miao")

class Dog(Mammal, Terrrestrial):
    def __init__(self):
        super().__init__('Dog')
        print('I am Dog with four legs')
    # method overriding
    # def make_sound(self):
    #     print("Sound: Bao, Bao")

class Mouse(Mammal):
    def __init__(self):
        super().__init__("Mouse")
        print('I am Mouse with four legs')
    # method overriding
    def make_sound(self):
        print("Sound: Cirr, Cirr")

def orchestra(animals):
    for animal in animals:
        animal.make_sound() # polymorphism


if __name__ == "__main__":
    d1 = Dog()
    c1 = Cat()
    orchestra([d1,c1, Mouse()])
