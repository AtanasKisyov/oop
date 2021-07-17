class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    @staticmethod
    def needed_fuel(km, consumption):
        return km * consumption

    def drive(self, km):
        fuel_to_burn = self.needed_fuel(km, self.fuel_consumption)
        if fuel_to_burn <= self.fuel:
            self.fuel -= fuel_to_burn
        return




