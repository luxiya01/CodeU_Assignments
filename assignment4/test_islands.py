#! /usr/bin/python3.5

# Author: Li Ling
# Last modified: 2017-06-25

import copy
import island_count
import unittest

class TestIslandCount(unittest.TestCase):
    def test_horizontal_count(self):
        landscape = [[1, 0, 1]]
        row = len(landscape)
        col = len(landscape[0])
        counter = island_count.IslandCounter(row, col, landscape)
        self.assertEqual(2, counter.count_islands())

    def test_vertical_count(self):
        landscape = [[1], 
                     [0], 
                     [1]]
        row = len(landscape)
        col = len(landscape[0])
        counter = island_count.IslandCounter(row, col, landscape)
        self.assertEqual(2, counter.count_islands())
        
    def test_diagonal_count(self):
        landscape = [[1, 0], 
                     [0, 1]]
        row = len(landscape)
        col = len(landscape[0])
        counter = island_count.IslandCounter(row, col, landscape)
        self.assertEqual(2, counter.count_islands())

    def test_basic_flood_fill_horizontal(self):
        landscape = [[1, 1, 0, 1, 1]]
        row = len(landscape)
        col = len(landscape[0])
        counter = island_count.IslandCounter(row, col, landscape)
        self.assertEqual(2, counter.count_islands())

    def test_basic_flood_fill_vertical(self):
        landscape = [[1], 
                     [1], 
                     [0], 
                     [1], 
                     [1]]
        row = len(landscape)
        col = len(landscape[0])
        counter = island_count.IslandCounter(row, col, landscape)
        self.assertEqual(2, counter.count_islands())

    def test_tricky(self):
        landscape = [[1, 0, 1, 1, 1],
                     [1, 1, 1, 0, 1],
                     [0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1]]
        row = len(landscape)
        col = len(landscape[0])
        counter = island_count.IslandCounter(row, col, landscape)
        self.assertEqual(1, counter.count_islands())

    def test_original_landscape_unmodified(self):
        landscape = [[1, 0, 1, 1, 1],
                     [1, 1, 1, 0, 1],
                     [0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1]]
        row = len(landscape)
        col = len(landscape[0])
        unmodified_landscape = copy.deepcopy(landscape)
        island_count.IslandCounter(row, col, landscape)
        for mod_row, unmod_row in zip(landscape, unmodified_landscape):
            self.assertListEqual(mod_row, unmod_row)

if __name__ == "__main__":
    unittest.main(verbosity=2)
