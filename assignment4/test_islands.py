#! /usr/bin/python3.5

# Author: Li Ling
# Last modified: 2017-06-25

import unittest
import islandCount

class TestIslandCount(unittest.TestCase):
    def setUp(self):
        self.row = 4
        self.col = 4
        self.landscape = [[False for x in range(self.col)] for y in range(self.row)]
        self.landscape[0][1] = True
        self.landscape[0][3] = True
        self.landscape[1][0] = True
        self.landscape[1][1] = True
        self.landscape[2][2] = True
        self.landscape[3][2] = True
        self.islandCounter = islandCount.IslandCounter(self.row, self.col, self.landscape)

    def testIslandCount(self):
        self.assertEqual(3, self.islandCounter.count_islands())

if __name__ == "__main__":
    unittest.main(verbosity=2)
