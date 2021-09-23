def trace_get_attributes(cls: type):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
        def __getattr__(self, item):
            result = getattr(self.wrapped, item)
            print(f"-- getting attribute '{item}' = {result}")
            return result
    return Wrapper
