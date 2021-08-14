from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.battle_field import BattleField


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, player_type, player_name):
        if player_type == "Beginner":
            player = Beginner(player_name)
        else:
            player = Advanced(player_name)
        self.player_repository.add(player)
        return f"Successfully added player of type {player_type} with username: {player_name}"

    def add_card(self, card_type, card_name):
        if card_type == "Magic":
            card = MagicCard(card_name)
        else:
            card = TrapCard(card_name)
        self.card_repository.add(card)
        return f"Successfully added card of type {card_type}Card with name: {card_name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attacker_name, enemy_name):
        attacker = self.player_repository.find(attacker_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        string_to_return = ""
        for player in self.player_repository.players:
            string_to_return += f"Username: {player.username} - Health: {player.health} - " \
                                f"Cards {len(player.card_repository.cards)}\n"
            for card in player.card_repository.cards:
                string_to_return += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return string_to_return
