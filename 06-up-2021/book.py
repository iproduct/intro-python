class Book:
    # next_id = 0
    def __init__(self, id, title, subtitle, authors, tags, year, language):
        # Book.next_id += 1
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.tags = tags
        self.year = year
        self.language = language

    def format(self):
        return f'| {self.id:4} | {self.title:35.35} | {self.subtitle:20.20} | {", ".join(self.authors):30.30} | ' \
               f'{", ".join(self.tags):30.30} | {self.year:6.6} | {self.language:7.7} |'

    def __str__(self):
        return f'Book({self.id}, {self.title}, {self.subtitle}, {self.authors}, ' \
               f'{self.tags}, {self.year}, {self.language})'
    def __repr__(self):
        return self.__str__()