from datetime import date, datetime, timedelta
from dataclasses import dataclass

from book import Book

@dataclass
class Borrowing:
    book_id: int
    borrow_date: date
    return_date: date

    def is_overdue(self) -> bool:
        return self.return_date < date.today()

@dataclass
class LibraryCard:
    """Class for keeping track of books borrowed by library Users"""
    id: int
    user_id: int
    borrowed_books : list[Borrowing]

    def get_overdue_borrowings(self):
        return filter(Borrowing.is_overdue, self.borrowed_books)

if __name__ == "__main__":
    lc1 = LibraryCard(1, 2, [])
    print(lc1)
    today = date.today()
    b1 = Borrowing(5, date(2021, 10,20), date(2021, 10,20) + timedelta(days=30))
    lc1.borrowed_books.append(b1)
    b2 = Borrowing(5, today, today + timedelta(days=30))
    lc1.borrowed_books.append(b2)
    print(lc1)
    print(list(lc1.get_overdue_borrowings()))