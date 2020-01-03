import node


class node_community_chest(node):
    def __init__(self, id, title, prev, next):
        node.__init__("community_chest")
        self.id = id,
        self.title = title
        self.prev = prev
        self.next = next
