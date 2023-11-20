from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
  def setUp(self):
    self.hero = Hero(
      username="Marian",
      level=10,
      health=100,
      damage=50
    )

  def test_initialization(self):
    self.assertEqual("Marian", self.hero.username)
    self.assertEqual(10, self.hero.level)
    self.assertEqual(100, self.hero.health)
    self.assertEqual(50, self.hero.damage)

  def test_battle_enemy_name_equals_to_username_rises_exception(self):

    with self.assertRaises(Exception) as ex:
      self.hero.battle(Hero("Marian", 10, 100, 50))

    self.assertEqual("You cannot fight yourself", str(ex.exception))

  def test_battle_health_equal_to_zero_rises_exception(self):
    self.hero.health = 0

    with self.assertRaises(ValueError) as ex:
      self.hero.battle(Hero("Ivan", 10, 100, 50))

    self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

  def test_battle_health_less_than_zero_rises_exception(self):
    self.hero.health = -1

    with self.assertRaises(ValueError) as ex:
      self.hero.battle(Hero("Ivan", 10, 100, 50))

    self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

  def test_battle_enemy_health_equals_to_zero_rises_exception(self):

    with self.assertRaises(ValueError) as ex:
      self.hero.battle(Hero("Ivan", 10, 0, 50))

    self.assertEqual("You cannot fight Ivan. He needs to rest", str(ex.exception))

  def test_battle_enemy_health_less_than_zero_rises_exception(self):

    with self.assertRaises(ValueError) as ex:
      self.hero.battle(Hero("Ivan", 10, -2, 50))

    self.assertEqual("You cannot fight Ivan. He needs to rest", str(ex.exception))

  def test_battle_heroes_both_health_zero_draw(self):
    self.hero.damage = 10

    result = self.hero.battle(Hero("Ivan", 10, 100, 10))
    self.assertEqual("Draw", result)

  def test_battle_heroes_both_health_less_than_zero_draw(self):
    result = self.hero.battle(Hero("Ivan", 10, 100, 60))
    self.assertEqual("Draw", result)

  def test_battle_heroes_hero_health_zero_enemy_health_minus_draw(self):
    result = self.hero.battle(Hero("Ivan", 10, 100, 10))
    self.assertEqual("Draw", result)

  def test_battle_heroes_hero_health_minus_zero_enemy_health_zero_draw(self):
    self.hero.damage = 10
    result = self.hero.battle(Hero("Ivan", 10, 100, 50))
    self.assertEqual("Draw", result)

  def test_battle_heroes_hero_wins_enemy_less_than_zero_health(self):
    result = self.hero.battle(Hero("Ivan", 10, 100, 5))

    self.assertEqual("You win", result)
    self.assertEqual(11, self.hero.level)
    self.assertEqual(55, self.hero.health)
    self.assertEqual(55, self.hero.damage)

  def test_battle_heroes_hero_wins_enemy_zero_health(self):
    self.hero.damage = 10
    result = self.hero.battle(Hero("Ivan", 10, 100, 5))

    self.assertEqual("You win", result)
    self.assertEqual(11, self.hero.level)
    self.assertEqual(55, self.hero.health)
    self.assertEqual(15, self.hero.damage)

  def test_battle_heroes_hero_loses_at_zero_health(self):
    self.hero.damage = 5

    enemy_hero = Hero("Ivan", 10, 100, 10)

    result = self.hero.battle(enemy_hero)

    self.assertEqual("You lose", result)
    self.assertEqual(11, enemy_hero.level)
    self.assertEqual(55, enemy_hero.health)
    self.assertEqual(15, enemy_hero.damage)

  def test_battle_heroes_hero_loses_at_minus_zero_health(self):
    self.hero.damage = 5

    enemy_hero = Hero("Ivan", 10, 100, 50)

    result = self.hero.battle(enemy_hero)

    self.assertEqual("You lose", result)
    self.assertEqual(11, enemy_hero.level)
    self.assertEqual(55, enemy_hero.health)
    self.assertEqual(55, enemy_hero.damage)

  def test__str__(self):
    result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
     f"Health: {self.hero.health}\n" \
     f"Damage: {self.hero.damage}\n"

    self.assertEqual(result, str(self.hero))

if __name__ == "__main__":
  main()