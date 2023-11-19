from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(fuel=55, horse_power=100)

    def test_default_fuel_consumption_class_attribute(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(55, self.vehicle.fuel)
        self.assertEqual(55, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_fuel_needed_less_than_fuel_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(56)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_correct_drive(self):

        self.vehicle.drive(10)
        self.assertEqual(42.5, self.vehicle.fuel)

    def test_refuel_fuel_above_fuel_capacity_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_refuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(5)

        self.assertEqual(55, self.vehicle.fuel)

    def test_correct_str_(self):
        expected_result = f"The vehicle has 100 " \
               f"horse power with 55 fuel left and 1.25 fuel consumption"
        result = str(self.vehicle)
        self.assertEqual(expected_result, result)

    if __name__ == "__main__":
        main()
      
