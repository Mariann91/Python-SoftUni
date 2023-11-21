from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @property
    @abstractmethod
    def get_added_price(self):
        ...

    def increase_price(self):
        self.price += self.get_added_price
      
