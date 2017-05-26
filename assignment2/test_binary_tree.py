#!/usr/bin/python3.5
import unittest
import binary_tree as btree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = btree.BinaryTree(0)
    
    def test_contain(self):
        """Note that if this test fails, then 
        both test_insert_left and test_insert_right 
        will also fail since they both use the contain method. """
        self.assertTrue(self.tree.contains(0))
        self.assertFalse(self.tree.contains(1))


    def test_insert_left(self):
        """Test whether inserting a left node is successful and 
        whether the data is actually stored in the tree after 
        the insertion. """
        self.assertFalse(self.tree.contains(1))
        self.assertTrue(0, self.tree.insert(1))
        self.assertTrue(self.tree.contains(1))

    def test_insert_right(self):
        """Same test as above but for insertion of a right node."""
        self.assertFalse(self.tree.contains(2))
        self.assertTrue(0, self.tree.insert(2, left=False))
        self.assertTrue(self.tree.contains(2))

if __name__ == "__main__":
    unittest.main(verbosity=2)
