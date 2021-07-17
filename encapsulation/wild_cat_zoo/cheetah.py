from wild_cat_zoo.animal import Animal


class Cheetah(Animal):

    COST = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Cheetah.COST)
        self.money_for_care = Cheetah.COST

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
