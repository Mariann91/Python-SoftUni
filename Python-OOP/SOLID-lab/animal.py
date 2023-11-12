class Animal:
    def __init__(self, species, sound):
        self.sound = sound
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals_list: list):
    for animal in animals_list:
        print(animal.sound)


animals = [Animal('cat', "meow"), Animal('dog', "woof-woof")]
animal_sound(animals)
