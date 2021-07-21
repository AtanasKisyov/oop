from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def calculate_distance(fuel, consumption, distance_to_travel):
        return distance_to_travel * consumption <= fuel

    def drive(self, distance):
        conditioner = distance * 0.9
        if self.calculate_distance(self.fuel_quantity, self.fuel_consumption, distance):
            self.fuel_quantity -= conditioner + (distance * self.fuel_consumption)

    def refuel(self, amount):
        self.fuel_quantity += amount


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def calculate_distance(fuel, consumption, distance_to_travel):
        return distance_to_travel * consumption <= fuel

    def drive(self, distance):
        conditioner = distance * 1.6
        if self.calculate_distance(self.fuel_quantity, self.fuel_consumption, distance):
            self.fuel_quantity -= self.fuel_consumption * distance + conditioner

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

