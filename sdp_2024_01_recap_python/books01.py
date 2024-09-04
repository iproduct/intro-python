
class Publication(object):
    def __init__(self, id: int = None, title: str = None, author: str = None, summary=None, keywords: tuple[str]=(),):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__summary = summary
        self.__keywords = keywords

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def summary(self):
        return self.__summary
    @summary.setter
    def summary(self, summary):
        self.__summary = summary

    @property
    def keywords(self):
        return self.__keywords
    @keywords.setter
    def keywords(self, keywords):
        self.__keywords = keywords

    def __str__(self):
        return f'{self.id}: {self.__title} - {self.__author} - {self.__summary} {self.__keywords}'

    def __repr__(self):
        return f'Publican({self.id}, {self.__title}, {self.__author}, {self.__summary}, {self.__keywords})'

if __name__ == '__main__':
    p1 = Publication(1, 'Fluent Python', 'Luciano Ramalho',
                     'Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you how to make your code shorter, faster, and more readable at the same time.',
                     ('python', 'programming'))
    old_keywords = p1.keywords
    p1.keywords = old_keywords + ('intermediate',)

    print(p1)