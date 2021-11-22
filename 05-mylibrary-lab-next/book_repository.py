
class IntIdSequence:
    def __init__(self):
        self.next_id = 0

    def __next__(self):
        self.next_id += 1
        return self.next_id

class BookRepository:
    def __init__(self, books = {}, id_sequence = None):
        self.books = books
        self.id_sequence = id_sequence

    def find_all(self):
        return list(self.books.values())

    def find_by_id(self, id):
        return self.books[id]

    def find_by_predicate(self, filter_predicate):
        return filter(filter_predicate, self.find_all())

    def find_by_name_part(self, name_part):
        return self.find_by_predicate(lambda book : name_part in book.title)

    def find_by_name_descr_part(self, part):
        return self.find_by_predicate(lambda book : part in book.title or part in book.descr)

    def find_by_authors_part(self, part):
        return self.find_by_predicate(lambda book : part in ",".join(book.authors))

    def insert(self, book):
        if self.id_sequence is not None:
            book.id = self.id_sequence.__next__()
        self.books[book.id] = book
        return book

    def update(self, book):
        self.books[book.id] = book
        return book

    def delete_by_id(self, id):
        removed = self.books[id]
        del self.books[id]
        return removed

    def count(self):
        return len(self.books)

