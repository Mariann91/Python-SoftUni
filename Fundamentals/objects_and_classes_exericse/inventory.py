class Inventory:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.left_capacity = self.__capacity
    self.items = []

  def add_item(self, item):
    if len(self.items) < self.__capacity:
      self.items.append(item)
      self.left_capacity -= 1
    else:
      return "not enough room in the inventory"

  def get_capacity(self):
    return self.__capacity

  def __repr__(self):
    items = ", ".join(self.items)
    return f"Items: {items}.\nCapacity left: {self.left_capacity}"
    
