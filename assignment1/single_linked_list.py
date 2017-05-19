class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList(object):
    """A single linked list class.
       
       Attribute: 
           head: the head node of the list. 
    """

    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        """Append a new node containing data 
        to the end of the single linked list. 

        Attribute: 
            data: the data contained in the new node"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

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
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next
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
        
    def get_list_from_index(self, index):
        """Returns a new linked list with the node at the 
        desired index as head. """
        head = self.get_node_from_index(index)
        return SingleLinkedList(head)

    def print(self):
        curr = self.head
        linked_list = []
        while curr != None:
            linked_list.append(curr.data)
            curr = curr.next
        print(linked_list)
