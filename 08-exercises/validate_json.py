from functools import wraps

from invalid_entity_data_exception import InvalidEntityDataException


def required_props(*expected_args):
    def decorator_valid_json(func):
        @wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            result = func(*args, **kwargs)
            for expected_arg in expected_args:
                if expected_arg not in result.__dict__ or [expected_arg] is None or not (result.__dict__[expected_arg]):
                    raise InvalidEntityDataException(f"Reqired proerty value '{expected_arg}' is missing or empty.")
            return result

        return wrapper_validate_json

    return decorator_valid_json


class Book:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"Book(title='{self.title})"


@required_props("title", "content")
def getBook(title, content):
    return Book(title, content)


if __name__ == '__main__':
    print(f"Book: {getBook('Python 3', 'Python content ...')}")
