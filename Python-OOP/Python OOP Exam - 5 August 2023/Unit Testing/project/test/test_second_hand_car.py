from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.second_hand_car = SecondHandCar(
            model="Mazda",
            car_type="2",
            mileage=97000,
            price=3300,
        )

    def test_correct_initialization(self):

        self.assertEqual("Mazda", self.second_hand_car.model)
        self.assertEqual("2", self.second_hand_car.car_type)
        self.assertEqual(97000, self.second_hand_car.mileage)
        self.assertEqual(3300, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_price_equals_to_one_rises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 1

        self.assertEqual(
            'Price should be greater than 1.0!',
            str(ve.exception)
        )

    def test_price_less_than_one_rises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 0

        self.assertEqual(
            'Price should be greater than 1.0!',
            str(ve.exception)
        )

    def test_mileage_equals_to_hundred_rises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 100

        self.assertEqual(
            'Please, second-hand cars only! Mileage must be greater than 100!',
            str(ve.exception)
        )

    def test_mileage_less_than_hundred_rises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 99

        self.assertEqual(
            'Please, second-hand cars only! Mileage must be greater than 100!',
            str(ve.exception)
        )

    def test_set_promotional_price_new_price_equals_to_price_rises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(3300)

        self.assertEqual(
            'You are supposed to decrease the price!',
            str(ve.exception)
        )

    def test_set_promotional_price_new_price_greater_than_price_rises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(3400)

        self.assertEqual(
            'You are supposed to decrease the price!',
            str(ve.exception)
        )

    def test_set_promotional_price(self):
        result = self.second_hand_car.set_promotional_price(3200)

        self.assertEqual(3200, self.second_hand_car.price)
        self.assertEqual(
            'The promotional price has been successfully set.',
            result
        )

    def test_need_repair_repair_price_greater_than_half_of_price(self):

        result = self.second_hand_car.need_repair(
            repair_price=1660,
            repair_description="accumulator change"
        )

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_correct_function(self):

        result = self.second_hand_car.need_repair(
            repair_price=1650,
            repair_description="accumulator change"
        )

        self.assertEqual(4950, self.second_hand_car.price)
        self.assertEqual(["accumulator change"], self.second_hand_car.repairs)
        self.assertEqual(
            'Price has been increased due to repair charges.',
            result
        )

    def test__gt__different_car_types(self):

        self.second_hand_car_other = SecondHandCar(
            model="Mazda",
            car_type="3",
            mileage=97000,
            price=3300,
        )

        result = self.second_hand_car > self.second_hand_car_other

        self.assertEqual(
            'Cars cannot be compared. Type mismatch!',
            result
        )

    def test_correct__gt__(self):

        self.second_hand_car_other = SecondHandCar(
            model="Mazda",
            car_type="2",
            mileage=97000,
            price=3400,
        )

        result = self.second_hand_car > self.second_hand_car_other

        self.assertEqual(False, result)

    def test__str__(self):

        self.assertEqual(
            f"""Model Mazda | Type 2 | Milage 97000km
Current price: 3300.00 | Number of Repairs: 0""",
            str(self.second_hand_car)
        )

if __name__ == "__main__":
    main()
  
