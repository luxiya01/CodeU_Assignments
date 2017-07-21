#!/usr/bin/python3.5
import unittest
import rearranging_cars

class TestRearrangingCars(unittest.TestCase):
    def setUp(self):
        self.initial = [1, 0, 2]

    def test_no_movements(self):
        moves = rearranging_cars.rearrange(self.initial, self.initial)
        self.assertEqual(0, len(moves))

    def test_one_movement(self):
        final = [1, 2, 0]
        expected_moves = [rearranging_cars.Movement(2, 2, 1)]
        actual_moves = rearranging_cars.rearrange(self.initial, final)
        self.assertMovementListEquals(expected_moves, actual_moves)

    def test_multiple_movements(self):
        final = [2, 0, 1]
        expected_moves = [rearranging_cars.Movement(1, 0, 1),
                          rearranging_cars.Movement(2, 2, 0),
                          rearranging_cars.Movement(1, 1, 2)]
        actual_moves = rearranging_cars.rearrange(self.initial, final)
        self.assertMovementListEquals(expected_moves, actual_moves)


    def assertMovementListEquals(self, expected_moves, actual_moves):
        self.assertEqual(len(expected_moves), len(actual_moves))
        for expected, actual in zip(expected_moves, actual_moves):
            self.assertEqual(expected.car, actual.car)
            self.assertEqual(expected.fro, actual.fro)
            self.assertEqual(expected.to, actual.to)

if __name__ == "__main__":
    unittest.main(verbosity=2)
