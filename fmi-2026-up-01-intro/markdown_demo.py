from rich.console import Console
from rich.markdown import Markdown

console = Console()
with open('rich_README.md', encoding='utf8') as f:
    renderable_markup = Markdown(f.read())
    console.print(renderable_markup)