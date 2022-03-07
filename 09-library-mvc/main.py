from tkinter import *

from controller.calculator_controller import CalculatorController
from dao.book_repository import BookRepository
from entity.book import Book
from service.book_service import BookService
from service.feet_to_meter_service import FeetToMeterService
from view.feet_to_meters import FeetToMeters
from view.utils.tkinter_utils import center_resize_window

if __name__ == "__main__":
    root = Tk()
    center_resize_window(root, 800, 400)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Configure doamin repos and services
    books_repo = BookRepository("books.json", Book)
    book_controller = BookService(books_repo)

    service = FeetToMeterService()
    controller = CalculatorController(service)
    feet_to_meters = FeetToMeters(root, controller)
    controller.view = feet_to_meters
    root.mainloop()
