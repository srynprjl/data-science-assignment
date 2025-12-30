class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, max):
        self.front = None
        self.back = None
        self.max = max
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if(self.size > self.max - 1):
            print("Queue full.")
            return None

        if not self.back:
            self.back = self.front = node
        else:
            self.back.next = node
            self.back = node
        self.size += 1
        print("Enqueued!")

    def dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        dequeue = self.front.data
        self.front = self.front.next

        if(self.front is None):
            self.back = None
        print("Dequeued!")
        self.size -= 1
        return dequeue

    def peek(self):
        if not self.front:
            return None
        return self.front.data

    def display(self):
        i = self.front
        while i is not None:
            print(f"{i.data}", end = " ")
            i = i.next
        print()

queue = Queue(max=5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.display()
print(queue.dequeue())
queue.display()
