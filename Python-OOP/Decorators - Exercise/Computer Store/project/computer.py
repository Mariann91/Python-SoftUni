from abc import ABC, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):

        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    @abstractmethod
    def computer_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    @abstractmethod
    def computer_type(self):
        ...

    @staticmethod
    def calculate_ram(input_ram):
        result = log2(input_ram)

        return ceil(result) == floor(result)

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.computer_processors:
            raise ValueError(f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        if not self.calculate_ram(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram

        self.price = self.computer_processors[processor] + int(log2(ram)) * 100

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
      
