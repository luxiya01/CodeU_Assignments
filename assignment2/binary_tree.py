class Node(object):
    """Defines one node in the binary tree. 

    Attributes: key, left node, right node. """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree(object):
    """Defines a binary tree. (NOT binary search tree). 

    Attributes:
        root: the node root of the binary tree.  """

    def __init__(self, key):
        self.root = Node(key)
