from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Food, Meat


class Mouse(Mammal):

    allowed_food = [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"Mouse does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):

    allowed_food = [Meat]

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"Dog does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):

    allowed_food = [Vegetable, Meat]

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food) not in self.allowed_food:
            return f"Cat does not eat {type(food).__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):

    allowed_food = [Meat]

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food) not in self.allowed_food:
            return f"Tiger does not eat {type(food).__name__}!"
        self.weight += food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
