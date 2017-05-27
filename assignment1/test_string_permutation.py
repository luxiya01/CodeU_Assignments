#!/usr/bin/python3.5
import unittest
import string_permutation as pmt

class TestStringPermutations(unittest.TestCase):

    def test_string_pmt_success(self):
        self.assertTrue(pmt.string_permutation("apple", "apple"))
        self.assertTrue(pmt.string_permutation("Apple", "apple"))
        self.assertTrue(pmt.string_permutation("apple", "papel"))
        self.assertTrue(pmt.string_permutation("Apple", "papel"))

    def test_string_pmt_empty_strings(self):
        self.assertTrue(pmt.string_permutation("", ""))
        self.assertFalse(pmt.string_permutation("", "apple"))

    def test_string_invalid_input(self):
        with self.assertRaises(ValueError):
            pmt.string_permutation("(^V^)", "^)V(^")
            pmt.string_permutation("Apple", "apple123")
            pmt.string_permutation("", "^)V(^")


if __name__ == "__main__":
    unittest.main(verbosity=2)

