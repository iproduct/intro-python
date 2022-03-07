from controller.book_controller import BookController
from controller.calculator_controller import CalculatorController


class AddBookCommand:
    def __init__(self, book_controller: BookController):
        self.book_controller = book_controller

    def __call__(self, *args, **kwargs):
        #TODO show add book dialog
        print("Showing 'Add Book' dialog")
