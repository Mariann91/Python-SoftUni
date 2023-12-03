from unittest import TestCase

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot(
            robot_id="robot",
            category="Military",
            capacity=5,
            price=5,
        )

    def test_class_attributes(self):
        self.assertEqual(
            ['Military', 'Education', 'Entertainment', 'Humanoids'],
            Robot.ALLOWED_CATEGORIES
        )

        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("robot", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(5, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_not_allowed_category_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "random"

        self.assertEqual(
            "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
            str(ve.exception)
        )

    def test_negative_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -2

        self.assertEqual(
            "Price cannot be negative!",
            str(ve.exception)
        )

    def test_upgrade_component_in_hardware_list_return_message(self):
        self.robot.hardware_upgrades.append("random part")

        result = self.robot.upgrade("random part", 50)

        self.assertEqual(
            "Robot robot was not upgraded.",
            result
        )

    def test_upgrade_component_added_to_hardware_list(self):

        result = self.robot.upgrade("random part", 50)

        self.assertEqual(["random part"], self.robot.hardware_upgrades)
        self.assertEqual(80, self.robot.price)
        self.assertEqual(
            result,
            'Robot robot was upgraded with random part.'
        )

    def test_update_not_update_message_max_software_updates_bigger_than_version(self):
        self.robot.software_updates.append(5)

        result = self.robot.update(3, 3)

        self.assertEqual(
            "Robot robot was not updated.",
            result
        )

    def test_update_not_update_message_not_enough_capacity(self):
        result = self.robot.update(3, 10)

        self.assertEqual(
            "Robot robot was not updated.",
            result
        )

    def test_update_correct_functon(self):
        result = self.robot.update(3, 4)

        self.assertEqual([3], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)
        self.assertEqual(
            'Robot robot was updated to version 3.',
            result
        )

    def test__gt__message_first_robot_greater_than_second(self):
        second_robot = Robot(
            robot_id="robot 2",
            category="Military",
            capacity=5,
            price=4,
        )

        result = self.robot > second_robot

        self.assertEqual(
            'Robot with ID robot is more expensive than Robot with ID robot 2.',
            result
        )

    def test__gt__message_first_robot_equal_to_second(self):
        second_robot = Robot(
            robot_id="robot 2",
            category="Military",
            capacity=5,
            price=5,
        )

        result = self.robot > second_robot

        self.assertEqual(
            'Robot with ID robot costs equal to Robot with ID robot 2.',
            result
        )

    def test__gt__message_else(self):
        second_robot = Robot(
            robot_id="robot 2",
            category="Military",
            capacity=5,
            price=6,
        )

        result = self.robot > second_robot

        self.assertEqual(
            'Robot with ID robot is cheaper than Robot with ID robot 2.',
            result
        )
