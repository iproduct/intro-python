books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни","O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 135.9)
    ]

#3
class Book(object):
    def __init__(self, id, title, subtitle, authors, publisher, year, price):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.price = price

    #4
    def __str__(self):
        return f'|{self.id:2d} | {self.title:20.20s} | {self.subtitle:25.25s} | {self.authors:25.25s} | {self.publisher:15.15s} | {self.year:4d} | {self.price:6.2f} | '

    def __repr__(self):
        return f'Book({self.id}, {self.title}, {self.subtitle}, {self.authors}, {self.publisher}, {self.year}, {self.price})'

if __name__ == '__main__':
    #1
    sum = 0
    for bt in books:
        print(f'|{bt[0]:2d} | {bt[1]:20.20s} | {bt[2]:25.25s} | {bt[3]:25.25s} | {bt[4]:15.15s} | {bt[5]:4d} | {bt[6]:6.2f} | ')
        sum += bt[6]

    #2
    print(f'Price: {sum:7.2f}')
    print(f'VAT  : {sum * 0.2:7.2f}')
    print(f'Total: {sum * 1.2:7.2f}')

    #5
    book_list = []
    for bt in books:
        book_list.append(Book(bt[0], bt[1], bt[2], bt[3], bt[4], bt[5], bt[6]))

    for book in book_list:
        print(book)
        # print(repr(book))
