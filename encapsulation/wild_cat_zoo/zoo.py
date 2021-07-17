from wild_cat_zoo.animal import Animal
from wild_cat_zoo.lion import Lion
from wild_cat_zoo.tiger import Tiger
from wild_cat_zoo.cheetah import Cheetah
from wild_cat_zoo.worker import Worker
from wild_cat_zoo.keeper import Keeper
from wild_cat_zoo.caretaker import Caretaker
from wild_cat_zoo.vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if not self.check_capacity(self.__animal_capacity, self.animals):
            return "Not enough space for animal"
        if not self.check_budget(self.__budget, price):
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.check_capacity(self.__workers_capacity, self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([x.salary for x in self.workers])
        if not self.check_budget(self.__budget, total_salaries):
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_price = sum([x.money_for_care for x in self.animals])
        if not self.check_budget(self.__budget, total_price):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_price
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        string_to_return = f"You have {len(self.animals)} animals\n"
        animals_dict = {}
        for animal in self.animals:
            if type(animal).__name__ not in animals_dict:
                animals_dict[type(animal).__name__] = []
            animals_dict[type(animal).__name__].append(animal)
        string_to_return += f"----- {len(animals_dict['Lion'])} Lions:\n"
        for animal in animals_dict['Lion']:
            string_to_return += f"{repr(animal)}\n"
        string_to_return += f"----- {len(animals_dict['Tiger'])} Tigers:\n"
        for animal in animals_dict['Tiger']:
            string_to_return += f"{repr(animal)}\n"
        string_to_return += f"----- {len(animals_dict['Cheetah'])} Cheetahs:\n"
        for animal in animals_dict['Cheetah']:
            string_to_return += f"{repr(animal)}\n"
        return string_to_return[:-1]

    def workers_status(self):
        string_to_return = f"You have {len(self.workers)} workers\n"
        workers_dict = {}
        for worker in self.workers:
            if type(worker).__name__ not in workers_dict:
                workers_dict[type(worker).__name__] = []
            workers_dict[type(worker).__name__].append(worker)
        string_to_return += f"----- {len(workers_dict['Keeper'])} Keepers:\n"
        for worker in workers_dict['Keeper']:
            string_to_return += f"{repr(worker)}\n"
        string_to_return += f"----- {len(workers_dict['Caretaker'])} Caretakers:\n"
        for worker in workers_dict['Caretaker']:
            string_to_return += f"{repr(worker)}\n"
        string_to_return += f"----- {len(workers_dict['Vet'])} Vets:\n"
        for worker in workers_dict['Vet']:
            string_to_return += f"{repr(worker)}\n"
        return string_to_return[:-1]

    @staticmethod
    def check_capacity(self, capacity, iterable):
        if len(iterable) >= capacity:
            return False
        return True

    @staticmethod
    def check_budget(budget, price):
        if budget - price <= 0:
            return False
        return True
