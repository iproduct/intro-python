from service.book_service import BookService


class BookController:
    def __init__(self, service: BookService, view=None):
        self.view = view
        self.service = service

    def reload_books(self):
        self.service.reload_books()

    def save_books(self):
        self.service.save_books()
