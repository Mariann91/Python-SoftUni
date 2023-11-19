from unittest import TestCase, main

from car_manager import Car


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Mazda", "2", 7, 45)

    def test_correct_initializing(self):
        self.assertEqual("Mazda", self.car.make)
        self.assertEqual("2", self.car.model)
        self.assertEqual(7, self.car.fuel_consumption)
        self.assertEqual(45, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_equals_to_empty_string_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_equal_to_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = 0

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_equals_to_empty_string_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_equal_to_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = 0

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_equal_to_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_below_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_equal_to_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_below_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_bellow_zero_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_negative_fuel_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_zero_fuel_rises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_correct_refuel_bellow_fuel_capacity(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

        self.car.refuel(45)
        self.assertEqual(45, self.car.fuel_amount)

    def test_drive_needed_fuel_less_than_fuel_amount_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        self.car.fuel_amount = 7
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    main()
