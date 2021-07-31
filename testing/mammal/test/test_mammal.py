from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.tiger = Mammal("George", "cat", "rawr")

    def test_correct_initialization(self):
        self.assertEqual("George", self.tiger.name)
        self.assertEqual("cat", self.tiger.type)
        self.assertEqual("rawr", self.tiger.sound)
        self.assertEqual("animals", self.tiger._Mammal__kingdom)

    def test_make_sound_method(self):
        self.assertEqual("George makes rawr", self.tiger.make_sound())

    def test_change_sound(self):
        self.assertEqual("rawr", self.tiger.sound)
        self.tiger.sound = "bark"
        self.assertEqual("bark", self.tiger.sound)

    def test_change_name(self):
        self.assertEqual("George", self.tiger.name)
        self.tiger.name = "Gosho"
        self.assertEqual("Gosho", self.tiger.name)

    def test_change_type(self):
        self.assertEqual("cat", self.tiger.type)
        self.tiger.type = "dog"
        self.assertEqual("dog", self.tiger.type)

    def test_get_kingdom_method(self):
        self.assertEqual("animals", self.tiger.get_kingdom())

    def test_info_method(self):
        self.assertEqual("George is of type cat", self.tiger.info())


if __name__ == "__main__":
    main()
