from testing.cat import Cat
from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Amador")

    def test_correct_initialization(self):
        self.assertEqual("Amador", self.cat.name, msg="Incorrect name on initialization")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size, msg="Incorrect size on initialization")

    def test_correct_size_increase_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size, msg="Incorrect size after 'eat' method is called")

    def test_cat_is_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_is_already_fed_raises(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_fall_asleep_if_not_fed_raises(self):
        self.assertFalse(self.cat.sleepy)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
