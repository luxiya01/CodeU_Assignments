#!/usr/bin/python3.5
import unittest
import binary_tree as btree

class TestAncestors(unittest.TestCase):
    def setUp(self):
        """This setup uses tree.insert, therefore tests in this file 
        shall only be performed after all tests in *test_binary_tree.py* are passed.
        
        The test tree is the same as provided in Q1 in assignment2. """
        self.tree = btree.BinaryTree(16)
        self.tree.insert(16, 9)
        self.tree.insert(16, 18, left=False)
        self.tree.insert(18, 19, left=False)
        self.tree.insert(9, 3)
        self.tree.insert(9, 14, left=False)
        self.tree.insert(3, 1)
        self.tree.insert(3, 5, left=False)

    def test_ancestors_root_node(self):
        """Root note shall not have ancestors"""
        self.assertListEqual([], self.tree.get_ancestors(16))
        
    def test_ancestors_nonexistent_node(self):
        with self.assertRaises(ValueError):
            self.tree.get_ancestors(100)

    def test_ancestors_non_root_node(self):
        """This is the example provided in Q1 in assignment2. """
        self.assertListEqual([3,9,16], self.tree.get_ancestors(5))

    def test_common_ancestor_nonexistent_node(self):
        with self.assertRaises(ValueError):
            self.tree.get_common_ancestor(5, 100)

    def test_common_ancestor_normal(self):
        """This is the example provided in Q2 in assignment2. """
        self.assertEqual(9, self.tree.get_common_ancestor(5, 14))

    def test_common_ancestor_special(self):
        """One of the nodes is the parent of the other. """
        self.assertEqual(9, self.tree.get_common_ancestor(3, 5))

    def test_common_ancestor_root(self):
        """Root node has no ancestor. """
        self.assertIsNone(self.tree.get_common_ancestor(16, 5))

if __name__ == "__main__":
    unittest.main(verbosity=2)
