
class MyList:
    def __init__(self, iterable = ()):
        self.values = list(iterable)
    def __getitem__(self, key):
        if isinstance(key, slice):
            # Get the start, stop, and step from the slice
            start, end, step = key.indices(len(self.values))
            print(start, end, step)
            return [self.values[i] for i in range(start, end, step)]
        elif isinstance(key, int):
            if key < 0:  # Handle negative indices
                key += len(self.values)
            if key < 0 or key >= len(self.values):
                raise IndexError("The index (%d) is out of range." % key)
            return self.values[key]  # Get the data from elsewhere
        else:
            raise TypeError("Invalid argument type.")

if __name__ == '__main__':
    mylist = MyList(range(10))
    print(mylist[2:7])
