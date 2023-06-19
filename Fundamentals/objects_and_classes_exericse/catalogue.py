class Catalogue:
  def __init__(self, name):
    self.name = name
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def get_by_letter(self, first_letter):
    first_letter_list = [word for word in self.products if word[0] == first_letter]
    return first_letter_list

  def __repr__(self):
    result = f"Items in the {self.name} catalogue:"

    for product in sorted(self.products):
      result += "\n" + product
    return result
      
