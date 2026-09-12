class FibIterator2:
    a, b = 0, 1
    def __init__(self, n):
        self.n = n
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        self.n -= 1
        return self.a
    def __iter__(self):
        return  self

if __name__ == '__main__':
    for n in FibIterable2(100):
        print(n)
    for n in FibIterator2(20):
        print(n)