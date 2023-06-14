class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        info = ""
        if species == "mammal":
            info = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            info = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            info = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"

        return info


zoo_name = input()
interval = int(input())

zoo = Zoo(zoo_name)

for _ in range(interval):
    animal_species, animal_name = input().split()

    zoo.add_animals(animal_species, animal_name)

called_species = input()

print(zoo.get_info(called_species))

