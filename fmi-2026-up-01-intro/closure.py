from typing import Callable


def create_counter(initial_value: int = 0) -> Callable[[], int]:
    count = initial_value
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

if __name__ == "__main__":
    counter = create_counter()
    for i in range(10):
        print(counter())