class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
            return

        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node


    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

dll=DoublyLinkedList()

dll.insert(10)
dll.insert(20)

dll.display()