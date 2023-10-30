from Shop.project.product import Product
from typing import List


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str or None:

        for product in self.products:

            if product.name == product_name:
                return product

    def remove(self, product_name):

        for product in self.products:

            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        return "\n".join([f'{product.name}: {product.quantity}' for product in self.products])
