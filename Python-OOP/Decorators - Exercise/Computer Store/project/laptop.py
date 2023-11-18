from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def computer_processors(self):
        processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

        return processors

    @property
    def max_ram(self):
        return 64

    @property
    def computer_type(self):
        return "laptop"
      
