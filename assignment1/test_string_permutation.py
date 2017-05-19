import unittest
import string_permutation as pmt

class TestStringPermutations(unittest.TestCase):
    def setUp(self):
        self.apple1 = "Apple"
        self.apple2 = "apple"
        self.apple3 = "papel"
        self.empty = ""

    def test_string_pmt_success(self):
        self.assertTrue(pmt.string_permutation(self.apple2, self.apple2))
        self.assertTrue(pmt.string_permutation(self.apple1, self.apple2))
        self.assertTrue(pmt.string_permutation(self.apple2, self.apple3))
        self.assertTrue(pmt.string_permutation(self.apple1, self.apple3))

    def test_string_pmt_empty_strings(self):
        self.assertTrue(pmt.string_permutation(self.empty, self.empty))
        self.assertFalse(pmt.string_permutation(self.empty, self.apple2))

if __name__ == "__main__":
    unittest.main()

