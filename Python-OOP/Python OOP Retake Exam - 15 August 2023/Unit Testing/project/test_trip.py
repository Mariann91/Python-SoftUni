from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self) -> None:

        self.trip = Trip(
            budget=200,
            travelers_number=5,
            is_family=True,
        )

    def test_DESTINATION_PRICES_PER_PERSON_class_attribute(self):
        self.assertEqual(
            {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500},
            self.trip.DESTINATION_PRICES_PER_PERSON
        )

    def test_initialization(self):
        self.assertEqual(200, self.trip.budget)
        self.assertEqual(5, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_equals_to_zero(self):

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_travelers_negative_number(self):

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = -1

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_if_travelers_are_less_than_two(self):
        test_instance = Trip(
            budget=200,
            travelers_number=1,
            is_family=True,
        )

        self.assertEqual(False, test_instance.is_family)

    def test_book_a_trip_destination_not_in_DESTINATION_PRICES_PER_PERSON(self):
        result = self.trip.book_a_trip("Greece")

        self.assertEqual(
            'This destination is not in our offers, please choose a new one!',
            result
        )

    def test_book_a_trip_budget_not_enough(self):
        result = self.trip.book_a_trip('New Zealand')

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_is_family_true_discount(self):
        self.trip.budget = 33750
        result = self.trip.book_a_trip('New Zealand')

        self.assertEqual(33750, self.trip.booked_destinations_paid_amounts['New Zealand'])
        self.assertEqual(
            f'Successfully booked destination New Zealand! Your budget left is 0.00',
            result
            )

    def test_book_a_trip_is_without_discount(self):
        self.trip.budget = 37500
        self.trip.is_family = False

        result = self.trip.book_a_trip('New Zealand')

        self.assertEqual(37500, self.trip.booked_destinations_paid_amounts['New Zealand'])
        self.assertEqual(
            f'Successfully booked destination New Zealand! Your budget left is 0.00',
            result
            )

    def test_booking_status_no_booked_destinations(self):

        result = self.trip.booking_status()

        self.assertEqual(
            'No bookings yet. Budget: 200.00',
            result
        )

    def test_booking_status(self):

        self.trip.budget = 59400

        self.trip.book_a_trip('New Zealand')
        self.trip.book_a_trip('Australia')

        expected_result = f"Booked Destination: Australia\n" \
                          f"Paid Amount: 25650.00\n" \
                          f"Booked Destination: New Zealand\n" \
                          f"Paid Amount: 33750.00\n" \
                          f"Number of Travelers: 5\n"\
                          f"Budget Left: 0.00"
      

        result = self.trip.booking_status()

        self.assertEqual(expected_result, result)
      
