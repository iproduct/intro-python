from functools import wraps
from typing import Callable, Any


def custom_cache(func: Callable) -> Callable:
    # Dictionary to store cached results
    storage = {}

    @wraps(func)  # Preserves the original function's name and docstring
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a hashable key from args and sorted kwargs items
        # Elements inside the arguments must be hashable (like ints, strings, tuples)
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key not in storage:
            # Cache miss: compute and store the result
            storage[cache_key] = func(*args, **kwargs)

        # Cache hit: return the stored result
        return storage[cache_key]

    # Optional: Attach a method to clear the cache manually
    def cache_clear() -> None:
        storage.clear()

    wrapper.cache_clear = cache_clear
    return wrapper


# --- Example Usage ---
@custom_cache
def expensive_calculation(x: int, y: int) -> int:
    print(f"Calculating for ({x}, {y})...")
    return x + y


print(expensive_calculation(4, 5))  # Triggers calculation
print(expensive_calculation(4, 5))  # Returns instantly from cache
