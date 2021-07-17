class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, qty):
        if self.quantity >= qty:
            self.quantity -= qty

    def increase(self, qty):
        self.quantity += qty
