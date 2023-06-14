class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        first_letter_products = []

        for product in self.products:
            if product[0] == first_letter:
                first_letter_products.append(product)
        return first_letter_products

    def __repr__(self):
        self.products.sort()

        result = "Items in the {0} catalogue:\n" \
                 "{1}".format(self.name, '\n'.join(self.products))
        return result
