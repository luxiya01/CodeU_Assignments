#!/usr/bin/python3.5
import unittest
import string_permutation as pmt

class TestStringPermutations(unittest.TestCase):
    def setUp(self):
        self.apple1 = "Apple"
        self.apple2 = "apple"
        self.apple3 = "papel"
        self.empty = ""
        self.invalid1 = "apple123"
        self.invalid2 = "(^V^)"
        self.invalid3 = "^)V(^"

    def test_string_pmt_success(self):
        self.assertTrue(pmt.string_permutation(self.apple2, self.apple2))
        self.assertTrue(pmt.string_permutation(self.apple1, self.apple2))
        self.assertTrue(pmt.string_permutation(self.apple2, self.apple3))
        self.assertTrue(pmt.string_permutation(self.apple1, self.apple3))

    def test_string_pmt_empty_strings(self):
        self.assertTrue(pmt.string_permutation(self.empty, self.empty))
        self.assertFalse(pmt.string_permutation(self.empty, self.apple2))

    def test_string_invalid_input(self):
        with self.assertRaises(ValueError):
            pmt.string_permutation(self.invalid2, self.invalid3)
            pmt.string_permutation(self.apple1, self.invalid1)
            pmt.string_permutation(self.empty, self.invalid3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

