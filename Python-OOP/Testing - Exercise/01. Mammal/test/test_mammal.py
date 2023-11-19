from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal(name="Tobi", mammal_type="Dog", sound="Woof")

    def test_correct_initialization(self):
        self.assertEqual("Tobi", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("Woof", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_correct_make_sound(self):
        self.assertEqual("Tobi makes Woof", self.mammal.make_sound())

    def test_correct_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_correct_info(self):
        self.assertEqual("Tobi is of type Dog", self.mammal.info())

if __name__ == "__main__":
    main()
  
