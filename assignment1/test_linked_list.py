#!/usr/bin/python3.5
import unittest
import single_linked_list as llist

class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.list_length = 10
        self.lst = llist.SingleLinkedList()
        for i in range(self.list_length):
            self.lst.append(i)

    def test_kth_element_from_head(self):
        for i in range(self.list_length):
            self.assertEqual(i, self.lst.get_index(i))

    def test_kth_element_from_last(self):
        for i in range(self.list_length):
            expected = self.list_length - i - 1
            self.assertEqual(expected, self.lst.get_kth_from_last(i))

if __name__ == "__main__":
    unittest.main(verbosity=2)
