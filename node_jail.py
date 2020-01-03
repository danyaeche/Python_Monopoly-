import node

class node_jail(node):
    def __init__(self, id, title, jail_bool, prev, next ):
        node.__init__("jail")
        self.id = id,
        self.title = title,
        self.jail_bool = jail_bool
        self.prev = prev
        self.next = next