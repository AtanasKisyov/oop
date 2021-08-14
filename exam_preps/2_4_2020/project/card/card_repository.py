class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        card_name = card.name
        card_check = [c.name for c in self.cards]
        if card_name in card_check:
            raise ValueError(f"Card {card_name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card_name):
        if card_name == "":
            raise ValueError("Card cannot be an empty string!")
        card = self.find(card_name)
        self.cards.remove(card)
        self.count -= 1

    def find(self, card_name):
        return [c for c in self.cards if c.name == card_name][0]
