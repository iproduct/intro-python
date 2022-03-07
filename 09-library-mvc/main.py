from tkinter import *

from controller.book_controller import BookController
from controller.calculator_controller import CalculatorController
from dao.book_repository import BookRepository
from entity.book import Book
from service.book_service import BookService
from service.feet_to_meter_service import FeetToMeterService
from view.main_view import MainView
from view.utils.tkinter_utils import center_resize_window

if __name__ == "__main__":
    root = Tk()
    center_resize_window(root, 800, 400)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Configure doamin repos and services
    books_repo = BookRepository("books.json", Book)
    book_service = BookService(books_repo)
    book_controller = BookController(book_service)
    book_controller.reload_books()

    main_view = MainView(root, book_controller)
    book_controller.view = main_view

    # Start the app event loop
    root.mainloop()
