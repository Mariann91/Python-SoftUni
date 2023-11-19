from unittest import TestCase, main

from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList("50", 1, False, 3.5, 2, 3)

    def test_initialization(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_correct_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_not_an_integer(self):

        with self.assertRaises(ValueError) as val:
            self.integer_list.add(3.5)

        self.assertEqual("Element is not Integer", str(val.exception))

    def test_correct_add_function(self):
        result = self.integer_list.add(4)

        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3, 4])

    def test_remove_index_index_out_of_range(self):

        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_correct_result(self):
        result = self.integer_list.remove_index(0)

        self.assertEqual(1, result)
        # judge
        self.assertEqual([2, 3], self.integer_list._IntegerList__data )

    def test_get_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct_item(self):
        correct_item = self.integer_list._IntegerList__data[0]

        self.assertEqual(correct_item, self.integer_list.get(0))

    def test_insert_index_out_of_range(self):

        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(4, 3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_value_not_an_integer(self):

        with self.assertRaises(ValueError) as val:
            self.integer_list.insert(0, 3.5)

        self.assertEqual("Element is not Integer", str(val.exception))

    def test_correct_insert_result(self):
        self.integer_list.insert(0, 0)

        self.assertEqual(0, self.integer_list._IntegerList__data[0])

    def test_correct_get_biggest(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_correct_get_index(self):
        self.assertEqual(0, self.integer_list.get_index(1))


if __name__ == "__main__":
    main()
