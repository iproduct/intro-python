

class Node:
    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev
    def __repr__(self):
        return f'({self.data}, {id(self.prev) if self.prev is not None else None}, {id(self.nxt) if self.nxt is not None else None})'

