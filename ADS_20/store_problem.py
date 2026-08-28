class Node:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.counter = None
        self.next = None


class queuesll:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_customer(self, customer_id):
        new_node = Node(customer_id)
        if customer_id % 2 == 1:
            new_node.counter = "Store A"
        else:
            new_node.counter = "Store B"

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def display(self):
        current = self.head
        while current is not None:

            print(
                f"Customer {current.customer_id} "
                f"-> {current.counter}"
            )

            current = current.next

queue = queuesll()
n = 10
for i in range(1, n + 1):
    queue.add_customer(i)

queue.display()