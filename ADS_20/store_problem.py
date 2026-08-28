class Node:
    def __init__(self,value):
       self.value=value 
       self.next=None

class Linked_list:
    def __init__(self):
        self.head = None
        self.count = 1

    def middle(self):
        middle= self.head
        current=self.head

        while current.next is not None:
            middle = middle.next
            current= current.next.next
        return middle

    def insertend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if self.count > 10:
            middle_node = self.middle()
            print(f"the middle node is: {middle_node.value}")
        current=self.head
        while current.next:
            current=current.next

        current.next= new_node
        self.count+=1

    
        

    def display(self):
        if self.count>10:
            store1 = []
            store2 = []
            middle_node = self.middle()
            current=self.head
            while current:
                for i in range(middle_node):
                    store1.append(current.value)
        print(" -> ".join(store1) + " -> None")
                

        
        store1=[]
        
        current=self.head
        while current:
            
            store1.append(str(current.value))
            current=current.next

        print(" -> ".join(store1) + " -> None")
        print(self.count)




stlist=Linked_list()



stlist.insertend(10)
stlist.insertend(20)
stlist.insertend(30)
stlist.insertend(40)
stlist.insertend(50)
stlist.insertend(60)
stlist.insertend(70)
stlist.insertend(80)
stlist.insertend(90)
stlist.insertend(100)
stlist.insertend(110)
stlist.insertend(110)


stlist.display()