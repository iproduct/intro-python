
class AddBookCommand:
    def __init__(self, book_controller):
        self.book_controller = book_controller

    def __call__(self, book):
        self.book_controller.add_book(book)
