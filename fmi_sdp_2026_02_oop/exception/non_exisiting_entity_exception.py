class NonExistingEntityException(Exception):
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return f"Entity does not exist exception: {self.message}"