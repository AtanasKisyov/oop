class Equipment:

    current_id = 0

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_id()

    @classmethod
    def get_id(cls):
        cls.current_id += 1
        return cls.current_id

    @staticmethod
    def get_next_id():
        return Equipment.current_id + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
