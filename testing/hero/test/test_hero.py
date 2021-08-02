from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Sandokan", 1, 100.0, 100.0)
        self.enemy_hero = Hero("Bad Sandokan", 1, 50.0, 10.0)

    def test_correct_initialization(self):
        self.assertEqual("Sandokan", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_correct_variable_types(self):
        self.assertTrue(isinstance(self.hero.username, str))
        self.assertTrue(isinstance(self.hero.level, int))
        self.assertTrue(isinstance(self.hero.health, float))
        self.assertTrue(isinstance(self.hero.damage, float))

    def test_battle_with_same_username_raises(self):
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_battle_with_low_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_low_enemy_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Bad Sandokan. He needs to rest", str(ve.exception))

    def test_battle_with_draw_case(self):
        self.hero.health = 5
        self.enemy_hero.health = 5
        expected = "Draw"
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, result)

    def test_battle_with_win_case(self):
        self.enemy_hero.health = 5
        expected = "You win"
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(95.0, self.hero.health)
        self.assertEqual(105.0, self.hero.damage)

    def test_battle_with_loose_case(self):
        self.hero.health = 1
        self.hero.damage = 1
        expected = "You lose"
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, result)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(54, self.enemy_hero.health)
        self.assertEqual(15, self.enemy_hero.damage)

    def test_string_method(self):
        expected = "Hero Sandokan: 1 lvl\n" \
                "Health: 100.0\n" \
                "Damage: 100.0\n"
        result = str(self.hero)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
