from need_for_speed.car import Car


class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION = 10

    def __init(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION
