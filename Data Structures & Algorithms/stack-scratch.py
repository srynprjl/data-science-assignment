class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, max):
        self.top = None
        self.max = max
        self.size = 0

    def push(self, data):
        if(self.size > self.max -1):
            print("Stack full.")
            return None

        node = Node(data)
        node.next = self.top
        self.top = node
        print("Pushed!")
        self.size += 1

    def pop(self):
        if not self.top:
            print("Stack is empty")
            return None

        pop = self.top.data
        self.top = self.top.next
        self.size -= 1
        print("Popped")
        return pop

    def top(self):
        if self.top:
            return self.top.data
        return None

    def display(self):
        i = self.top
        while i is not None:
            print(f"{i.data}", end=" ")
            i = i.next
        print()

stack = Stack(max=5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.display()

print(f"Popped Item: {stack.pop()}")
stack.display()
