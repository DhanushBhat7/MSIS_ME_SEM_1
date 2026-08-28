class queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue) == 0

    def push(self,value):
        print(f"Pushed: {value}")
        self.queue.append(value)
        return 

    def pop(self):
        if self.is_empty():
                raise IndexError("Queue is empty!! nothing to pop.")
        return print(f"The popped element is: {self.queue.pop(0)}")

    def size(self):
        return len(self.queue)

    def display(self):
        return print("the elements in the queue are: ", self.queue)


my_queue = queue()

my_queue.push(10)
my_queue.push(20)
my_queue.push(30)
my_queue.push(40)

my_queue.pop()
my_queue.push(50)

my_queue.pop()
my_queue.pop()
my_queue.pop()
my_queue.pop()

my_queue.pop()    #index-error

my_queue.display()