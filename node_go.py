import node

class node_go(node):
    def __init__(self, id, prev, next):
        node.__init__("go")
        self.id = id
        self.prev = prev
        self.next = next



