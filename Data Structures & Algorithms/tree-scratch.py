class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def display(self):
        print(f" {"    " * self.get_level()} -- {self.data}" )
        for i in self.children:
            i.display()

print("Childs of Root")
a = Node(1)
b = Node(2)
c = Node(3)
a.add_child(b)
a.add_child(c)
a.display()


print("Adding Childs for 2")
d = Node(4)
e = Node(5)

f = Node(6)
g = Node(7)

b.add_child(d)
b.add_child(e)
a.display()

print("Adding childs of 3")

c.add_child(f)
c.add_child(g)
a.display()
print()
