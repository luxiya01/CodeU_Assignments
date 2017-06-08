#! /usr/bin/python3.5

class Dictionary(object):
    """A dictionary class holding a word dictionary as a list
    and implements the two functions isWord and isPrefix. """

    def __init__(self, wordList):
        """The dictionary contains words given in the wordList. 
        It also constructs a prefixSet given the wordList.
        No duplicates exist in wordSet and prefixSet. 
        Assumes that the dictionary will NOT be modified once created.
        """
        self.wordSet = set(wordList)
        self.prefixSet = self.generatePrefixSet(self.wordSet)

    def isWord(self, string):
        """Time complexity: O(1)"""
        return string in self.wordSet

    def isPrefix(self, string):
        """Time complexity: O(1)"""
        return string in self.prefixSet


    def generatePrefixSet(self, wordSet):
        """Returns a prefixSet generated using the wordSet. 
        Time complexity: O(m*n) 
                         where m = len(wordSet)
                               n = len(longest word in wordSet)
        """
        prefixSet = set()
        for word in wordSet:
           currentPrefix = []
           for letter in word: 
               currentPrefix.append(letter)
               prefixSet.add(''.join(currentPrefix))
        return prefixSet


