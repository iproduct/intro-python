class BTNode[T]:
    def __init__(self, val: T, parent: 'BTNode[T]' = None, left: 'BTNode[T]'=None, right: 'BTNode[T]'=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
