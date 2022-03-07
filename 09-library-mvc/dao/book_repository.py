from dao.json_repository import JsonRepository
from dao.repository import Repository
from entity.book import Book


class BookRepository(JsonRepository):
    def find_by_title(self, title_part: str) -> list[Book]:
        title_part_lower = title_part.lower()
        books_list = self.find_all()
        results = [book for book in books_list if title_part_lower in book.title.lower()]
        return results

    def find_by_author(self, author_part: str) -> list[Book]:
        author_part_lower = author_part.lower()
        books_list = self.find_all()
        results = []
        for book in books_list:
            for author in book.authors:
                if author_part_lower in author.lower():
                    results.append(book)
                    break
        return results
