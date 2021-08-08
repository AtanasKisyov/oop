from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.pf = PaintFactory("Factory", 10)

    def test_correct_initialization(self):
        expected = "Factory"
        result = self.pf.name
        self.assertEqual(expected, result)
        expected = 10
        result = self.pf.capacity
        self.assertEqual(expected, result)
        expected = ["white", "yellow", "blue", "green", "red"]
        result = self.pf.valid_ingredients
        self.assertEqual(expected, result)
        expected = {}
        result = self.pf.ingredients
        self.assertEqual(expected, result)

    def test_add_ingredient_raises_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient("pink", 200)
        expected = "Ingredient of type pink not allowed in PaintFactory"
        result = str(te.exception)
        self.assertEqual(expected, result)

    def test_add_ingredient_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient("white", 11)
        expected = "Not enough space in factory"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_add_ingredient_correct(self):
        self.pf.add_ingredient("white", 1)
        expected = {"white": 1}
        result = self.pf.ingredients
        self.assertEqual(expected, result)

    def test_remove_ingredient_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient("white", 1)
        expected = "'No such ingredient in the factory'"
        result = str(ke.exception)
        self.assertEqual(expected, result)

    def test_remove_ingredient_raises_value_error(self):
        self.pf.add_ingredient("white", 1)
        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient("white", 2)
        expected = "Ingredients quantity cannot be less than zero"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_remove_ingredient_correct(self):
        self.pf.add_ingredient("white", 9)
        self.pf.remove_ingredient("white", 8)
        expected = {"white": 1}
        result = self.pf.ingredients
        self.assertEqual(expected, result)

    def test_products_property(self):
        self.pf.add_ingredient("blue", 2)
        expected = {"blue": 2}
        result = self.pf.products
        self.assertEqual(expected, result)

    def test_can_add_correct(self):
        expected = False
        result = self.pf.can_add(11)
        self.assertEqual(expected, result)

    def test_represent_method(self):
        self.pf.add_ingredient("white", 1)
        self.pf.add_ingredient("blue", 2)
        expected = "Factory name: Factory with capacity 10.\n" \
                   "white: 1\n" \
                   "blue: 2\n"


if __name__ == "__main__":
    main()
