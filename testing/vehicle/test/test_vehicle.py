from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.car = Vehicle(10.0, 90.5)

    def test_correct_initialization(self):
        self.assertEqual(10.0, self.car.fuel)
        self.assertEqual(90.5, self.car.horse_power)
        self.assertEqual(10.0, self.car.capacity)
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method(self):
        self.car.drive(2)
        self.assertEqual(7.5, self.car.fuel)

    def test_drive_method_raises(self):
        with self.assertRaises(Exception) as e:
            self.car.drive(200)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel_method(self):
        self.car.fuel = 0
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel)

    def test_refuel_method_raises(self):
        with self.assertRaises(Exception) as e:
            self.car.refuel(200)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_string_method(self):
        expected = "The vehicle has 90.5 " \
               "horse power with 10.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.car))

    def test_types(self):
        self.assertTrue(isinstance(self.car.fuel, float))
        self.assertTrue(isinstance(self.car.capacity, float))
        self.assertTrue(isinstance(self.car.horse_power, float))
        self.assertEqual(isinstance(self.car.fuel_consumption, float))


if __name__ == "__main__":
    main()
