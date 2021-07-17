class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer = [x for x in self.customers if x.id == subscription.customer_id][0]
        trainer = [x for x in self.trainers if x.id == subscription.trainer_id][0]
        plan = [x for x in self.plans if x.id == subscription.exercise_id][0]
        equipment = [x for x in self.equipment if x.id == plan.equipment_id][0]
        return f"{repr(subscription)}\n{customer}\n{trainer}\n{equipment}\n{plan}"
