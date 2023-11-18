from unittest import TestCase, main

from main import Worker


class WorkerTests(TestCase):
  
    def setUp(self) -> None:
        self.worker = Worker(name="TestGuy", salary=1000, energy=100)

    def test_correct_initializing(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increase_worker_money(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_decrease_worker_energy(self):
        energy = self.worker.energy

        self.worker.work()
        self.assertEqual(energy - 1, self.worker.energy)

    def test_energy_bellow_zero(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_method(self):
        energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(energy, self.worker.energy)

    def test_get_info(self):

        self.assertEqual('TestGuy has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()
