
class circular:

    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enque(self,value):
        if self.size == self.capacity:
            print("Queue is full !! Increasing size of the queue")
            self.increase_capacity()

        self.queue[self.rear] = value
        self.rear = (self.rear+1) % self.capacity
        self.size+=1

    def deque(self):
        if self.size == 0:
            print("queue is empty!! nothing to deque")
            return None
        value = self.queue[self.front]
        self.queue[self.front]=None
        self.front = (self.front+1) % self.capacity
        self.size-=1
        return value

    def increase_capacity(self):
        old_capacity = self.capacity
        self.capacity = self.capacity*2
        new_queue = [None] * self.capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front+i) % old_capacity]

        self.queue = new_queue

        self.front = 0
        self.rear = self.size

        print(f"Capacity Increased from {old_capacity} to {self.capacity}")

    def display(self):
        print("\n Queue: ", self.queue)
        print("\n size: ", self.size)
        print("\n Front: ", self.front)
        print("\n Rear: ", self.rear)
        print("\n Limit: ", self.capacity)


q = circular(7)

q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
q.enque(50)


q.display()

q.deque()
q.deque()

q.display()

q.enque(30)
q.enque(40)
q.enque(50)

q.display()

q.enque(60)
q.enque(70)

q.display()

q.enque(90)

q.display()

