from wild_cat_zoo.animal import Animal


class Lion(Animal):

    COST = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Lion.COST)
        self.money_for_care = Lion.COST

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
