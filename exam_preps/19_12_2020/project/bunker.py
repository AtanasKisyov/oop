class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def filer(iterable, object_type, error_message):
        result = [obj for obj in iterable if obj.__class__.__name__ == object_type]
        if not result:
            raise IndexError(error_message)
        return result

    @property
    def food(self):
        object_type = "FoodSupply"
        error_message = "There are no food supplies left!"
        food = self.filer(self.supplies, object_type, error_message)
        return food

    @property
    def water(self):
        object_type = "WaterSupply"
        error_message = "There are no water supplies left!"
        water = self.filer(self.supplies, object_type, error_message)
        return water

    @property
    def painkillers(self):
        object_type = "Painkiller"
        error_message = "There are no painkillers left!"
        painkiller = self.filer(self.supplies, object_type, error_message)
        return painkiller

    @property
    def salves(self):
        object_type = "Salve"
        error_message = "There are no salves left!"
        salve = self.filer(self.supplies, object_type, error_message)
        return salve

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if not survivor.needs_healing:
            return
        last_medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        self.medicine.remove(last_medicine)
        last_medicine.apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if not survivor.needs_sustenance:
            return
        last_sustenance = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
        self.supplies.remove(last_sustenance)
        last_sustenance.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
