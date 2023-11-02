class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):

        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):

        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):

        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)

                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_needed = sum(worker.salary for worker in self.workers)

        if money_needed <= self.__budget:
            self.__budget -= money_needed

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum(animal.money_for_care for animal in self.animals)

        if money_needed <= self.__budget:
            self.__budget -= money_needed

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        map_function = {
            "Lion": lambda x: lions.append(x),
            "Tiger": lambda x: tigers.append(x),
            "Cheetah": lambda x: cheetahs.append(x),
        }

        [map_function[animal.__class__.__name__](animal) for animal in self.animals]

        lions_info = "\n".join(lion.__repr__() for lion in lions)
        tigers_info = "\n".join(tiger.__repr__() for tiger in tigers)
        cheetah_info = "\n".join(cheetah.__repr__() for cheetah in cheetahs)

        return f"You have {len(self.animals)} animals\n" + \
            f"----- {len(lions)} Lions:\n" + \
            f"{lions_info}\n" + \
            f"----- {len(tigers)} Tigers:\n" + \
            f"{tigers_info}\n" + \
            f"----- {len(cheetahs)} Cheetahs:\n" + \
            f"{cheetah_info}"

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        map_function = {
            "Keeper": lambda x: keepers.append(x),
            "Caretaker": lambda x: caretakers.append(x),
            "Vet": lambda x: vets.append(x),
        }

        [map_function[worker.__class__.__name__](worker) for worker in self.workers]

        keepers_info = "\n".join(keeper.__repr__() for keeper in keepers)
        caretakers_info = "\n".join(caretaker.__repr__() for caretaker in caretakers)
        vets_info = "\n".join(vet.__repr__() for vet in vets)

        return f"You have {len(self.workers)} workers\n" + \
            f"----- {len(keepers)} Keepers:\n" + \
            f"{keepers_info}\n" + \
            f"----- {len(caretakers)} Caretakers:\n" + \
            f"{caretakers_info}\n" + \
            f"----- {len(vets)} Vets:\n" + \
            f"{vets_info}"
