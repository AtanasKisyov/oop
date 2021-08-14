from project.card.card import Card


class MagicCard(Card):

    def __init__(self, card):
        super().__init__(card, 5, 80)
