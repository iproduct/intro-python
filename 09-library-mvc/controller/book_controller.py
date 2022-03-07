from service.book_service import BookService


class BookController:
    def __init__(self, service: BookService, view=None):
        self.view = view
        self.service = service

    def get_all_books(self):
        return self.service.get_all_books()

    def reload_books(self):
        return self.service.reload_books()

    def save_books(self):
        return self.service.save_books()
