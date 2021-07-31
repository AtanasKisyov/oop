from testing.list import IntegerList
from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4, 5, 6.5, "Pesho")

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3, 4, 5], self.list._IntegerList__data)

    def test_add_method_working_correct(self):
        self.list.add(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.list._IntegerList__data)
        with self.assertRaises(ValueError) as ve:
            self.list.add("Pesho")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_method_working_correct(self):
        self.list.remove_index(0)
        self.assertEqual([2, 3, 4, 5], self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(100)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_working_correct(self):
        self.assertEqual(4, self.list.get(3))
        with self.assertRaises(IndexError) as ie:
            self.list.get(100)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_working_correct(self):
        self.list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ie:
            self.list.insert(7, 0)
        self.assertEqual("Index is out of range", str(ie.exception))
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "Pesho")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_method_working_correct(self):
        self.assertEqual(5, self.list.get_biggest())

    def test_get_index_method_working_correct(self):
        self.assertEqual(4, self.list.get_index(5))


if __name__ == "__main__":
    main()
