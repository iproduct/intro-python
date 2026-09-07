import inspect
from functools import wraps
from typing import Callable, Any


def selective_cache(*cached_params: str) -> Callable:
    """
    A cache decorator that only uses specified parameter names to construct the cache key.

    If no parameter names are provided, it defaults to using all parameters.
    """

    def decorator(func: Callable) -> Callable:
        storage = {}
        # Get the function's signature to map args and kwargs to parameter names
        sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # 1. Bind the incoming arguments to their parameter names
            bound_args = sig.bind(*args, **kwargs)
            # 2. Apply default parameter values for any arguments not explicitly passed
            bound_args.apply_defaults()

            # 3. Determine which parameters to use for the cache key
            # If cached_params is empty, use all parameters defined in the function
            targets = cached_params if cached_params else bound_args.arguments.keys()

            # 4. Construct the cache key by extracting the targeted values in a sorted order
            try:
                key_items = tuple((name, bound_args.arguments[name]) for name in sorted(targets))
                cache_key = key_items
            except KeyError as e:
                raise ValueError(
                    f"Parameter '{e.args[0]}' specified in @selective_cache does not exist "
                    f"in the signature of function '{func.__name__}'."
                )

            # 5. Check cache storage
            if cache_key not in storage:
                storage[cache_key] = func(*args, **kwargs)

            return storage[cache_key]

        # Attach a helper to clear the cache manually
        def cache_clear() -> None:
            storage.clear()

        wrapper.cache_clear = cache_clear
        return wrapper

    return decorator
