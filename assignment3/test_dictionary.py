#! /usr/bin/python3.5

import unittest
import dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.wordList = ['CAR', 'CAR', 'CARD', 'CART', 'CAT']
        self.prefixSet = ['C', 'CA', 'CAR', 'CARD', 'CART', 'CAT']
        self.testDict = dictionary.Dictionary(self.wordList)

    def testWordSetConstruction(self):
        self.assertCountEqual(set(self.wordList), self.testDict.wordSet)

    def testPrefixSetConstruction(self):
        self.assertCountEqual(self.prefixSet, self.testDict.prefixSet)

    def testIsWordTrue(self):
        for word in self.wordList:
            self.assertTrue(self.testDict.isWord(word))

    def testIsWordFalse(self):
        self.assertFalse(self.testDict.isWord('CA'))

    def testIsPrefixTrue(self):
        for prefix in self.prefixSet:
            self.assertTrue(self.testDict.isPrefix(prefix))

    def testIsPrefixFalse(self):
        self.assertFalse(self.testDict.isPrefix('R'))

if __name__ == "__main__":
    unittest.main(verbosity=2)
