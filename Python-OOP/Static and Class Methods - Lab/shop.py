from typing import Dict


class Shop:

    def __init__(self, name: str, shop_type: str, capacity: int) -> None:
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    def add_item(self, item_name: str):
        if sum(self.items.values()) == self.capacity:
            return "Not enough capacity in the shop"

        if item_name not in self.items:
            self.items[item_name] = 0

        self.items[item_name] += 1

        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        
        if self.items[item_name] <= 0:
            self.items.pop(item_name)

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def small_shop(cls, name: str, shop_type: str) -> object:
        return cls(name, shop_type, capacity=10)
