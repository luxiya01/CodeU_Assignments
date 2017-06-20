#! /usr/bin/python3.5

import unittest
import wordSearcher
import dictionary

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.dict = dictionary.Dictionary(['CAR', 'CARD', 'CART', 'CAT'])
        self.char2dArray = [['A', 'A', 'R'], ['T', 'C', 'D']]
        self.row = len(self.char2dArray)
        self.col = len(self.char2dArray[0])
        self.word_searcher = wordSearcher.WordSearcher(self.row, self.col, self.char2dArray, self.dict)

    def testFindAllWords(self):
        """All words in expected shall be in actual. 
        All words in actual shall also be in expected. """
        expected = set(['CAR', 'CARD', 'CAT'])
        actual = self.word_searcher.findAllWords()
        self.assertCountEqual(expected, actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)
