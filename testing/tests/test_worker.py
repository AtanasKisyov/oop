from testing.worker import Worker

from unittest import TestCase, main


class WorkerTest(TestCase):

    def setUp(self):
        self.worker = Worker("Pesho", 50, 10)

    def test_correct_initialization(self):
        self.assertEqual("Pesho", self.worker.name, msg="Incorrect name on initialization")
        self.assertEqual(50, self.worker.salary, msg="Incorrect salary on initialization")
        self.assertEqual(10, self.worker.energy, msg="Incorrect energy on initialization")
        self.assertEqual(0, self.worker.money, msg="Incorrect amount of money on initialization")

    def test_correct_rest_method(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.rest()
        self.assertEqual(11, self.worker.energy, msg="Class method 'rest' is not working properly")

    def test_incorrect_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception), msg="Class method 'work' is not working properly")

    def test_correct_money_increase_after_work_method(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(50, self.worker.money, msg="Incorrect money after work method is called")

    def test_correct_energy_decrease_after_work_method(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.work()
        self.assertEqual(9, self.worker.energy, msg="Incorrect energy after work method is called")

    def test_correct_get_info_method(self):
        self.worker.work()
        self.assertEqual("Pesho has saved 50 money.", self.worker.get_info())


if __name__ == "__main__":
    main()
