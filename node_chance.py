import node

class node_chance(node):
    def __init__(self, id, title, prev, next):
        node.__init__("chance")
        self.id = id,
        self.title = title
        self.prev = prev
        self.next = next