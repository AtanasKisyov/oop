class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.validate_password_length(value) and self.validate_upper_case(value) and self.validate_digit(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @staticmethod
    def validate_password_length(password):
        return len(password) >= 8

    @staticmethod
    def validate_upper_case(password):
        upper_case = [x for x in password if x.isupper()]
        return True if upper_case else False

    @staticmethod
    def validate_digit(password):
        digit = [x for x in password if x.isdigit()]
        return True if digit else False

    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"
