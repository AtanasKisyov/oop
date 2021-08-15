from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.pf = PaintFactory("Neftohim", 10)

    def test_correct_initialization(self):
        self.assertEqual("Neftohim", self.pf.name)
        self.assertEqual(10, self.pf.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)
        self.assertEqual({}, self.pf.ingredients)

    def test_add_ingredient_raises_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient("black", 2)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(te.exception))

    def test_add_ingredient_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient("white", 11)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_correct(self):
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.pf.ingredients)

    def test_remove_ingredient_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient("white", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_raises_value_error(self):
        self.pf.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient("white", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_correct(self):
        self.pf.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.pf.ingredients)
        self.pf.remove_ingredient("white", 1)
        self.assertEqual({"white": 0}, self.pf.ingredients)

    def test_products_property(self):
        self.pf.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.pf.products)

    def test_repr_method(self):
        self.pf.add_ingredient("white", 1)
        expected = "Factory name: Neftohim with capacity 10.\nwhite: 1\n"
        result = repr(self.pf)
        self.assertEqual(expected, result)

    def test_can_add(self):
        self.assertTrue(self.pf.can_add(7))
        self.assertFalse(self.pf.can_add(11))


if __name__ == "__main__":
    main()
