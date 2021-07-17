class Customer:

    current_id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_id()

    @classmethod
    def get_id(cls):
        cls.current_id += 1
        return cls.current_id

    @staticmethod
    def get_next_id():
        return Customer.current_id + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
