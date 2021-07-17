class Pizza:

    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}
        self.__topping_objects = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value
    
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity
    
    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        topping_name = topping.topping_type
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping_name not in self.toppings:
            self.toppings[topping_name] = 0
        self.toppings[topping_name] += topping.weight
        self.__topping_objects.append(topping)

    def calculate_total_weight(self):
        return sum([x.weight for x in self.__topping_objects]) + self.__dough.weight
