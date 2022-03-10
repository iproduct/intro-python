
class ShowAddBookCommand:
    def __init__(self, book_controller):
        self.book_controller = book_controller

    def __call__(self, *args, **kwargs):
        self.book_controller.show_add_book()
