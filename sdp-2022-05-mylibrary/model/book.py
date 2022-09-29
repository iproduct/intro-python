import uuid

class Book:
    def __init__(self, title = None, description = None, author = None, id = None):
        self.id = id
        self.title = title
        self.description = description
        self.author = author

    def __str__(self):
        return f"| {self.id!s:>28} | {self.title:<40} | {self.desrtiption!s:<12} | {self.author!s:<15} |"

