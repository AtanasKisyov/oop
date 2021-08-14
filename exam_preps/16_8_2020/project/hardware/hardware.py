class Hardware:

    def __init__(self, name, type_of_hardware, capacity, memory):
        self.name = name
        self.type = type_of_hardware
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_capacity = 0
        self.used_memory = 0

    def check_space(self, software_capacity, software_memory):
        future_memory = software_memory + self.used_memory
        future_capacity = software_capacity + self.used_capacity
        if self.memory >= future_memory and self.capacity >= future_capacity:
            return True
        return False

    def install(self, software):
        if not self.check_space(software.capacity_consumption, software.memory_consumption):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)
        self.used_memory += software.memory_consumption
        self.used_capacity += software.capacity_consumption

    def uninstall(self, software):
        self.software_components.remove(software)
        self.used_memory -= software.memory_consumption
        self.used_capacity -= software.capacity_consumption
