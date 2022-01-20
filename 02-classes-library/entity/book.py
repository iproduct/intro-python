class Book:
    next_id = 0  # unique id sequence

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, title=None, subtitle=None, authors=tuple(), isbn=None, publisher=None,
                 year=None, price=None, genre=None, tags=tuple(), description=None):
        # Book.next_id += 1
        # self.__class__.next_id += 1
        self.id = self.__class__.get_next_id()
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.price = price
        self.genre = genre
        self.tags = tags
        self.description = description

    def __str__(self):
        return f"| {self.id:>3d} | {self.title:<20.20s} | {self.subtitle:<20.20s} | " \
               f"{', '.join(self.authors):<20.20s} | {self.isbn:<10.10s} | " \
               f"{self.publisher:<10.10s} | {self.price:<6.2f} | {self.year:<10.10s} | " \
               f"{self.genre:<10.10s} | {', '.join(self.tags):<15.15s} |"

