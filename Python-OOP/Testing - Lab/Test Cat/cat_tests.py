from unittest import TestCase, main

from main import Cat


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat(name="Cat")

    def test_initialization_of_cat(self):
        self.assertEqual("Cat", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_validate_cat_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_is_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_is_not_sleepy_after_sleeping(self):

        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
  
