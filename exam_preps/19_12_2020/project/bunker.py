class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = [food for food in self.supplies if food.__class__.__name__ == "FoodSupply"]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water = [water for water in self.supplies if water.__class__.__name__ == "WaterSupply"]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [pk for pk in self.medicine if pk.__class__.__name__ == "Painkiller"]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [salve for salve in self.medicine if salve.__class__.__name__ == "Salve"]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        survivor_names = [s.name for s in self.survivors]
        current_survivor = survivor.name
        if current_survivor in survivor_names:
            raise ValueError(f"Survivor with name {current_survivor} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            last_medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
            last_medicine.apply(survivor)
            self.medicine.remove(last_medicine)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            last_sustenance = [m for m in self.supplies if m.__class__.__name__ == sustenance_type][-1]
            last_sustenance.apply(survivor)
            self.supplies.remove(last_sustenance)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")

