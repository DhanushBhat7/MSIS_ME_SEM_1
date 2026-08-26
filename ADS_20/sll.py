class node: 
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node        

    def display(self):

        if not self.head:
            print('List is empty!!')
        current= self.head
        elements=[]

        while current:
            elements.append(str(current.value))
            current=current.next

        print(" -> ".join(elements) + " -> None")

        return

    def insertend(self, value):
        new_node=node(value) 
        if not self.head:
            self.head=new_node
            return

        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def insertmid(self,value,position):
        new_node=node(value)
        if not self.head:
            self.head=new_node
            return
        count=0
        current=self.head
        while count !=position-1:
            current=current.next
            count+=1
        new_node.next=current.next
        current.next=new_node

    def delete(self):
        self.head=self.head.next

    def deletemid(self,position):
        count=1
        current=self.head
        while count !=position-1:
            current=current.next
            count+=1
        current.next=current.next.next

    def deleteend(self):
        if self.head is None:
            print('List is Empty')
        current=self.head
        while current.next.next:
            current=current.next
        current.next=None

    def search(self, key):
        current=self.head
        count=1
        while current:
            if current.value==key:
                print(f'value is found at:{count} position')
                break
            current=current.next
            count+=1
        


            


ll=LinkedList()

ll.insert(10)
ll.insertend(20)
ll.insertend(30)
ll.insertend(40)
ll.insertend(50)
ll.insertmid(15,1)
ll.display()
ll.delete()
ll.deletemid(2)
ll.deleteend()
ll.display()

ll.search(40)