from wild_cat_zoo.animal import Animal


class Tiger(Animal):

    COST = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Tiger.COST)
        self.money_for_care = Tiger.COST

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
