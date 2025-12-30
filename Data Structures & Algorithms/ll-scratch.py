class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        print(f"Added {data} at the start")
        return self.head

    def insert_at_end(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        print(f"Added {data} at the end")

    def insert(self, data, index):
        if(index == 0):
            self.insert_at_start(data)
            return
        last = self.head
        for i in range(index -1):
            if last.next is None:
                print("Index is out of bounds. ")
                return
            last = last.next
        node = Node(data)
        node.next = last.next
        last.next = node
        print(f"Added {data} at index {index}")

    def delete(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head == temp.next
            return
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        if not temp:
            return

        prev.next = temp.next
        print(f"Removed {data}")

    def traverse(self):
        head = self.head
        list = f"{ head.data } "
        while head.next:
            list += f" -> {head.next.data}"
            head = head.next
        print(list)

    def get(self, index):
        temp = self.head
        for i in range(index):
            if i is not None:
                temp = temp.next
            else:
                break
        return temp.data

l = LinkedList()
l.insert_at_end(10)
l.insert_at_end(12)
l.insert_at_end(14)
l.insert_at_end(3)
l.insert_at_end(12)
l.insert_at_start(3)
l.insert(11, 2)

l.traverse()
l.delete(11)

print(f"{l.get(2)} is in index 2")

l.traverse()
