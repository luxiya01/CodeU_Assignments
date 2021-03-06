class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList(object):
    """A single linked list class.
       
       Attribute: 
           head: the head node of the list. Initialized to None
                 if the parameter is not provided. 
           tail: the tail node of the list. Initialized to the 
                 value of head. 
    """

    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0

    def append(self, data):
        """Append a new node containing data 
        to the end of the single linked list. 

        Attribute: 
            data: the data contained in the new node"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, data):
        """ If a node with the specified data exists in 
        the linked list, remove it. If multiple nodes 
        with the specified data exist, only the first 
        node of such nodes will be removed.

        Attribute: 
            data: the data to be removed"""
        prev = None
        curr = self.head
        while curr != None:
            if curr.data == data:
                self.size -= 1
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return curr
            else: 
                prev = curr
                curr = curr.next
        return None

    def get_node_from_index(self, index):
        """Returns the node at the valid index. """
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr

    def get_index(self, index):
        """Returns the data of the node at the valid index, 
        assumes zero indexing. """
        return self.get_node_from_index(index).data 

    def get_kth_from_last(self, backward_index):
        """Returns the data of a node. When counting from 
        the last element in the linked list backwards, the 
        node whose value is returned has index equal to 
        backward_index."""
        index = self.size - backward_index - 1
        return self.get_index(index)
        
    def print(self):
        curr = self.head
        linked_list = []
        while curr != None:
            linked_list.append(curr.data)
            curr = curr.next
        print(linked_list)
