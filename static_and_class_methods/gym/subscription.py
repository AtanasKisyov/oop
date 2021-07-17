class Subscription:

    current_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.get_id()

    @classmethod
    def get_id(cls):
        cls.current_id += 1
        return cls.current_id

    @staticmethod
    def get_next_id():
        return Subscription.current_id + 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
