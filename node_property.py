import node

class node_property(node):
    def __init__(self, id, color, title, price, prev, next):
        node.__init__("property")
        self.id = id
        self.color = color
        self.title = title
        self.price = price
        self.houses = []
        self.hotel = []
        self.prev = prev
        self.next = next

