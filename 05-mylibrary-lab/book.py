class Book:
    """Book model class"""
    def __init__(self, title, subtitle, authors, isbn, publisher, year, price, genre="programming", tags=[],
                 description=None):
        self.id = None
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.price = price
        self.genre = genre
        self.tags = tags
        self.description = description

    def __repr__(self):
        line1 = f"| {self.id:^3d} | {self.title:<20.20s} | {self.subtitle:<20.20s} | " \
        f"{', '.join(self.authors):^25.25s} | {self.isbn:^10.10s} | {self.publisher:^10.10s} " \
        f"| {self.year:<4d} | {self.price:>7.2f} | {self.genre:^15.15s} | {', '.join(self.tags):^30.30s} |"
        len_line1 = len(line1) - 4
        line2 = f"| {self.description:^{len_line1}.{len_line1}s} |"
        return line1 + "\n" + line2

    def __str__(self):
        return f"| {self.id:^3d} | {self.title:<20.20s} | {self.subtitle:<20.20s} | " \
               f"{', '.join(self.authors):^25.25s} | {self.isbn:^10.10s} | {self.publisher:^10.10s} " \
               f"| {self.year:<4d} | {self.price:>7.2f} | {self.genre:^15.15s} | {', '.join(self.tags):^30.30s} |"

    def get_vat_price(self):
        if not hasattr(self, "vat_price"):
            self.vat_price = 1.2 * self.price
        return self.vat_price


if __name__ == "__main__":
    b1 = Book(
        "Head First Python",
        "A Brain-Friendly Guide",
        ["Paul Barry"],
        "1491919531",
        "O'Reilly UK Ltd.",
        2016,
        41.82,
        "Software Engineering",
        [
            "python",
            "introduction",
            "examples",
            "programming"
        ],
        "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    )
    b2 = Book(
        "Head First Python",
        "A Brain-Friendly Guide",
        ["Paul Barry"],
        "1491919531",
        "O'Reilly UK Ltd.",
        2016,
        41.82,
        description="Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    )
    # print(b1.__dict__)
    # b1.get_vat_price()
    # print(b1.__dict__)
    # print(Book.__dict__)
    # print(b1)
    # print(b2)
