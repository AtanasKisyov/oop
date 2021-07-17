from need_for_speed.vehicle import Vehicle
from need_for_speed.family_car import FamilyCar
from need_for_speed.motorcycle import MotorCycle
from need_for_speed.car import Car
from need_for_speed.sport_car import SportCar
from need_for_speed.race_motorcycle import RaceMotorcycle
from need_for_speed.cross_motorcycle import CrossMotorcycle


vehicle = CrossMotorCycle(50, 150)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(2)
print(vehicle.fuel)
# family_car = FamilyCar(150, 150)
# family_car.drive(50)
# print(family_car.fuel)
# family_car.drive(50)
# print(family_car.fuel)
# print(family_car.__class__.__bases__[0].__name__)
