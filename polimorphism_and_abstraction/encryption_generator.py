class EncryptionGenerator:

    VALID_RANGE = range(32, 127)

    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        string_to_return = ""
        for char in self.text:
            ascii_code = ord(char) + other
            if ascii_code > 126:
                ascii_code -= 95
            if ascii_code < 32:
                ascii_code += 95
            string_to_return += chr(ascii_code)
        return string_to_return
