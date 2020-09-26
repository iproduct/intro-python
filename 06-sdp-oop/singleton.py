import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""

    cls.__instance = None
    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cl, *args, **kwargs):
        if cl.__instance is None:
            cl.__instance = cl.__new_original__(cl)
            cl.__instance.__init_original__(*args, **kwargs)
        return cl.__instance

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__

    return cls


@singleton
class TheOne:
    """TheOne class is a singleton example class"""
    def __init__(self, name='Python'):
        self.name = name
    def __str__(self):
        return f'The one: {self.name}!'

if __name__ == '__main__':
    the_one1 = TheOne('Python')
    the_one2 = TheOne('Go')
    print(id(the_one1))
    print(id(the_one2))
    # the_one2.name = 'John'
    print(the_one1)
    print(the_one1 == the_one2)
    print(the_one1.__class__)