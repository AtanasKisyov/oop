from testing.car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Hyundai", "Santa Fe", 10, 100)

    def test_correct_initialization(self):
        self.assertEqual("Hyundai", self.car.make)
        self.assertEqual("Santa Fe", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_incorrect_make_raises(self):
        with self.assertRaises(Exception) as e:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(e.exception))

    def test_incorrect_model_raises(self):
        with self.assertRaises(Exception) as e:
            self.car.model = 0
        self.assertEqual("Model cannot be null or empty!", str(e.exception))

    def test_incorrect_fuel_consumption(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_consumption = -200
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(e.exception))

    def test_incorrect_fuel_capacity(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(e.exception))

    def test_incorrect_fuel_amount(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_amount = -202
        self.assertEqual("Fuel amount cannot be negative!", str(e.exception))

    def test_refuel_method_correct(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refuel_method_incorrect(self):
        with self.assertRaises(Exception) as e:
            self.car.refuel(-20)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(e.exception))

    def test_drive_method_correct(self):
        self.car.refuel(100)
        self.car.drive(50)
        self.assertEqual(95, self.car.fuel_amount)

    def test_drive_method_incorrect(self):
        with self.assertRaises(Exception) as e:
            self.car.refuel(2)
            self.car.drive(200)
        self.assertEqual("You don't have enough fuel to drive!", str(e.exception))


if __name__ == "__main__":
    main()
