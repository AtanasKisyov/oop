class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, ml):
        if self.size - self.quantity - ml <= 0:
            return
        self.quantity += ml

    def status(self):
        return self.size - self.quantity
