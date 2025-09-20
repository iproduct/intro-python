from functools import wraps


def singleton(cls):
    """Make a class Singleton that has only one instance."""
    @wraps(cls)
    def singleton_wrapper(*args, **kwargs):
        if singleton_wrapper._instance is None:
            singleton_wrapper._instance = cls(*args, **kwargs)
            # singleton_wrapper._instance.__class__ = cls
        return singleton_wrapper._instance
    singleton_wrapper._instance = None
    return singleton_wrapper
