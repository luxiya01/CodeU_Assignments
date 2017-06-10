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
        """Worst case time complexity: O(n) 
        where n = number of nodes in the tree. """
        return self.contains_helper(self.root, key)

    def contains_helper(self, node, key):
        """Preorder tree traversal."""
        if node.key == key: 
            return True
        lnode = False
        rnode = False
        if node.left:
            lnode = self.contains_helper(node.left, key)
        if not lnode and node.right: 
            rnode = self.contains_helper(node.right, key)
        return lnode or rnode

    def insert(self, parent_key, key, left=True):
        """If left = True, then the node will be inserted to the left 
        of the parent node. 
        
        If the parent already has a child at the desired direction, 
        then that child node will be replaced by a new node with 
        both left and right = None.

        Worst case time complexity: O(n) where n = number of nodes in the tree
        (O(n) for self.contains(parent_key) + O(n) for self.contains(key) 
        + O(n) for self.insert_helper = O(3n) = O(n))
        """
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
        if not lnode and node.right: 
            rnode = self.insert_helper(node.right, parent_key, key, left)
        return lnode or rnode

    def get_ancestors(self, key):
        if not self.contains(key):
            raise ValueError("The given key does not exist!")
        ancestor_nodes,_ = self.get_ancestors_helper([self.root], key)
        ancestors = [node.key for node in ancestor_nodes]
        ancestors.reverse()
        return ancestors

    def get_ancestors_helper(self, nodelst, key):
        """Preorder traversal. 
        Returns a list of ancestor nodes. """
        curr = nodelst.pop()
        if curr.key == key: 
            return nodelst, True
        nodelst.append(curr)
        if curr.left: 
            nodelst.append(curr.left)
            leftlst, leftfound = self.get_ancestors_helper(nodelst, key)
            if leftfound:
                return leftlst, leftfound
        if curr.right: 
            nodelst.append(curr.right)
            rightlst, rightfound = self.get_ancestors_helper(nodelst, key)
            if rightfound: 
                return rightlst, rightfound
        return nodelst.pop(), False

    def get_common_ancestor(self, key1, key2):
        """Note that a node is NOT considered ancestor of itself. 
        This is to be consistent with Q1. 
        If one of the keys given is that of the root, 
        common ancestor will be None. 
        """
        ancestors_node1 = self.get_ancestors(key1)
        ancestors_node2 = self.get_ancestors(key2)
        if len(ancestors_node1)== 0 or len(ancestors_node2)==0:
            return None
        for i in ancestors_node1:
            if i in ancestors_node2:
                return i
        return None
