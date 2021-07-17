class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        capacity = 15
        return capacity

    @staticmethod
    def customer_capacity():
        capacity = 10
        return capacity

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers][0]
        dvd = [x for x in self.dvds][0]
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers = '\n'.join([repr(x) for x in self.customers])
        dvds = '\n'.join([repr(x) for x in self.dvds])
        return f"{customers}\n{dvds}"
