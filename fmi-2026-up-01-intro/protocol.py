from typing import Protocol

# 1. Define the Protocol
class Drawable(Protocol):
    def draw(self) -> str:
        ...  # Use ellipses for method bodies in Protocols

# 2. Implement classes (No explicit inheritance from Drawable required)
class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return 10

# 3. Use the Protocol as a type hint
def render(shape: Drawable):
    print(shape.draw())

# Works with both classes because they follow the "structure"
render(Circle())  # Output: Drawing a circle
render(Square())  # Output: Drawing a square