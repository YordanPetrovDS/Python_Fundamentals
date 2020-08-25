class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            animals = self.mammals
            species_name_plural = "Mammals"
        elif species == "fish":
            animals = self.fishes
            species_name_plural = "Fishes"
        elif species == "bird":
            animals = self.birds
            species_name_plural = "Birds"
        return (
            f'{species_name_plural} in {self.name}: {", ".join(animals)}\n'
            f'Total animals: {Zoo.__animals}'
        )


zoo_name = input()
animals_count = int(input())
zoo = Zoo(zoo_name)

for i in range(animals_count):
    species, animal = input().split(" ", maxsplit=2)
    zoo.add_animals(species, animal)

print(zoo.get_info(input()))
