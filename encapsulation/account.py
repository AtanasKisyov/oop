class Account:

    def __init__(self, account_id, balance, pin):
        self.__id = account_id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if not pin == self.__pin:
            return "Wrong pin"
        return self.__id

    def change_pin(self, old, new):
        if not old == self.__pin:
            return "Wrong pin"
        self.__pin = new
        return "Pin changed"
