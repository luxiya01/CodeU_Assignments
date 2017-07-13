#!/usr/bin/python3.5
import unittest
import unknown_language

class TestUnknownLanguage(unittest.TestCase):
    def test_one_letter(self):
        """In this case, the entire dictionary contains only one alphabet. """
        word_list = ['A', 'AA', 'AAA']
        test_language = unknown_language.UnknownLanguage(word_list)
        expected = ['A']
        self.assertListEqual(expected, test_language.topological_sort())

    def test_upper_lower_case(self):
        """Check upper and lower case are treated as different alphabets. """
        word_list = ['A', 'a']
        test_language = unknown_language.UnknownLanguage(word_list)
        self.assertListEqual(word_list, test_language.topological_sort())

    def test_definite_order(self):
        """In this case, there is only one correct order. """
        word_list = ['A', 'a', 'B', 'b', 'C', 'c']
        test_language = unknown_language.UnknownLanguage(word_list)
        self.assertListEqual(word_list, test_language.topological_sort())

    def test_ambiguous_order(self):
        """In this case, there is no way to determine the ordering of *C*."""
        word_list = ['AR', 'RT', 'TC']
        test_language = unknown_language.UnknownLanguage(word_list)
        actual = test_language.topological_sort()
        self.assertTrue(comes_before(actual, 'A', 'R'))
        self.assertTrue(comes_before(actual, 'R', 'T'))

    def test_ambiguous_order2(self):
        """In this case, there is no way to determine whether A comes before T
        or the other way around. """
        word_list = ['ART', 'RAT', 'CAT', 'CAR']
        test_language = unknown_language.UnknownLanguage(word_list)
        actual = test_language.topological_sort()
        self.assertTrue(comes_before(actual, 'A', 'R'))
        self.assertTrue(comes_before(actual, 'T', 'R'))
        self.assertTrue(comes_before(actual, 'R', 'C'))

    def test_words_diff_length(self):
        """Check the algorithm against words of different length. """
        word_list = ['AaAaAaAa', 'aAA']
        test_language = unknown_language.UnknownLanguage(word_list)
        expected = ['A', 'a']
        self.assertListEqual(expected, test_language.topological_sort())

def comes_before(lst, fst, snd):
    """Check whether fst comes before snd in the list lst."""
    fount_fst = False
    for elem in lst:
        if elem == fst:
            fount_fst = True
        if elem == snd:
            return fount_fst

if __name__ == "__main__":
    unittest.main(verbosity=2)
