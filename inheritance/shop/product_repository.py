from shop.product import Product
from shop.drink import Drink
from shop.food import Food


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self):
        return "\n".join(f'{x.name}: {x.quantity}' for x in self.products)
