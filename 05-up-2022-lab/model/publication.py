class Publication(object):
    def __init__(self, id: int, title: str, author: str, publisher: str, year: int):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year


    def __repr__(self):
        book_attr_list = [f'{p[0]} = {p[1]}' for p in self.__dict__.items()]
        book_attr_str = ', '.join(book_attr_list)
        return f"Publication({book_attr_str})"
