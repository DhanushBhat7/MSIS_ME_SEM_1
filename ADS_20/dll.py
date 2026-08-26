class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
            return

        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        self.tail=new_node


    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def insertend(self,value):
        new_node = node(value)
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        new_node.prev=current
        self.tail=new_node
    
    def insertmid(self,value,key):
        new_node= node(value)
        current =self.head
        count =0
        while key-1 != count:
            current=current.next
            count+=1
        current.prev.next=new_node
        new_node.prev=current.prev
        current.prev=new_node
        new_node.next=current

    def delete(self):
        current=self.tail
        current.prev.next = None
        current.prev=self.tail

    def deletebegin(self):
        current=self.head.next
        current.prev = None
        self.head.next = None
        self.head = current
        

    def deletemid(self,key):
        current =self.head
        count =0
        while key-1 != count:
            current=current.next
            count+=1

        current.prev.next = current.next
        current.next.prev = current.prev
        current.prev=None
        current.next=None

        

dll=DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insertend(30)
dll.insertend(60)
dll.insertend(70)
dll.insertend(80)
dll.display()
dll.insertmid(15,2)
dll.display()
dll.delete()
dll.display()
dll.deletebegin()
dll.display()
dll.deletemid(3)
dll.display()