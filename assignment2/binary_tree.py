class Node(object):
    """Defines one node in the binary tree. 

    Attributes: key, left node, right node. """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree(object):
    """Defines a binary tree. (NOT binary search tree). 
    Does not allow duplicated keys. 

    Attributes:
        root: the node root of the binary tree.  """

    def __init__(self, key):
        self.root = Node(key)

    def contains(self, key):
        return self.contains_helper(self.root, key)

    def contains_helper(self, node, key):
        """Preorder tree traversal."""
        if node.key == key: 
            return True
        lnode = False
        rnode = False
        if node.left:
            lnode = self.contains_helper(node.left, key)
        if node.right: 
            rnode = self.contains_helper(node.right, key)
        return lnode or rnode

    def insert(self, parent_key, key, left=True):
        """If left = True, then the node will be inserted to the left 
        of the parent node. """
        if not self.contains(parent_key):
            raise ValueError("The desired parent key does not exist.")
        if self.contains(key):
            raise ValueError("The key to-be-inserted already exists!")
        return self.insert_helper(self.root, parent_key, key, left)

    def insert_helper(self, node, parent_key, key, left):
        """Preorder traversal"""
        if node.key == parent_key: 
            if left: 
                node.left = Node(key)
            else: 
                node.right = Node(key)
            return True
        lnode = False
        rnode = False
        if node.left: 
            lnode = self.insert_helper(node.left, parent_key, key, left)
        if node.right: 
            rnode = self.insert_helper(node.right, parent_key, key, left)
        return lnode or rnode

