class Stack:
    def __init__(self):
        self.stack=[]

    def isempty(self):
        return len(self.stack) == 0

    def top(self):
        if len(self.stack)== 0:
            print("stack is empty!!")
        return self.stack[-1]

    def append(self,value):
        self.stack.append(value)
        print(f"Pushed: {value}")

    def pop(self):
        if self.isempty():
            raise IndexError("stack is empty!! nothing to pop.")
        return print("Pop Item: ",self.stack.pop())

    def size(self):
        return len(self.stack)

    def display(self):
        return print("The elements in the stack are :",self.stack)

my_stack = Stack()

my_stack.append(10)
my_stack.append(20)
my_stack.append(30)
my_stack.append(40)

print(f"The top of the stack is: {my_stack.top()} ")

my_stack.display()

my_stack.pop()
my_stack.pop()

my_stack.display()

my_stack.pop()
my_stack.append(50)

my_stack.display()
print("The length of the stack is: ",my_stack.size())

my_stack.pop()
my_stack.pop()

