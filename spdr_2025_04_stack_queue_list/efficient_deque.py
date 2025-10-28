
class Deque:
    def __init__(self, max_elements):
        self.max_elements = max_elements
        self.elements = list(range(max_elements))
        self.start = self.end = 0

    def append(self, element):
        if self.end == self.max_elements:
            raise Exception('Deque is full')
        self.elements[self.end % self.max_elements] = element

    def pop(self):
        pass