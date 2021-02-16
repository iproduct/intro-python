class Document:
    def __init__(self, id, title, subtitle, authors, tags, language):
        # Book.next_id += 1
        # has_a == composition
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.tags = tags
        self.language = language

        def __str__(self):
            return f'{self.id}, {self.title}, {self.subtitle}, {self.authors}, ' \
                   f'{self.tags}, {self.language}'

        def __repr__(self):
            return self.__str__()

class Book(Document): # is_a == inheritance
    # next_id = 0
    def __init__(self, id, title, subtitle, authors, tags, year, language):
        super().__init__(id, title, subtitle, authors, tags, language)
        # Book.next_id += 1
        # has_a == composition
        self.year = year
        self._internal = "don't export - protected"

    def format(self):
        return f'| {self.id:4} | {self.title:35.35} | {self.subtitle:20.20} | {", ".join(self.authors):30.30} | ' \
               f'{", ".join(self.tags):30.30} | {self.year:6.6} | {self.language:7.7} |'

    def __str__(self):
        return f'Book({super().__str__()}, {self.year})'

    def __eq__(self, other):
        self.id == other.id

    def get_internal(self):
        return self._internal
