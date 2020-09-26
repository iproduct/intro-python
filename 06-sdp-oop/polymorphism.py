from points import Point

# Interface declaration
class InfiniteSeries(object):
    def next(self): raise NotImplementedError('next')

# Implementations
class Fibonacci(InfiniteSeries):
    def __init__(self): self.n1, self.n2 = 1, 1
    def next(self):
        n = self.n1
        self.n1, self.n2 = self.n2, self.n1 + self.n2
        return n

class Geometric(InfiniteSeries):
    def __init__(self, divisor=2.0):
        self.n = 1.0 / divisor
        self.nt = self.n / divisor
        self.divisor = divisor
    def next(self):
        n = self.n
        self.n += self.nt
        self.nt /= self.divisor
        return n

class Letters(InfiniteSeries):
    def __init__(self):
        self.next_letter = 'a'
    def next(self):
        result = self.next_letter
        self.next_letter = chr(ord(self.next_letter) + 1);
        return result;

class Points(InfiniteSeries):
    def __init__(self):
        self.next_point = Point(0, 0)

    def next(self):
        result = self.next_point
        self.next_point = Point(self.next_point.x + 1, self.next_point.y + 1);
        return result;

def test_series(series, number = 10):
    for i in range(number):
        print(series.next()),
    print()

if __name__=='__main__':
    test_series(Fibonacci())
    test_series(Geometric(3))
    test_series(Letters())
    test_series(Points())
    # test_series(InfiniteSeries())

