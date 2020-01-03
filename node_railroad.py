import node

class node_railrode(node):
    def __init__(self, id, title, price, prev, next):
        node.__init__("railroad")
        self.id = id
        self.title = title
        self.price = price
        self.prev = prev
        self.next = next