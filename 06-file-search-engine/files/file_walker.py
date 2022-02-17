import os
from typing import Iterable
from re import Pattern, compile
from os import DirEntry


def walk_files_in_dir(dir_: str = '.', *, regex: Pattern | str | None = None, recursive: bool = False) -> Iterable[DirEntry]:
    """
    Create a lazy generator walking all files in a directory recursively
    :param dir_: directory to walk
    :param regex: regext filename filter
    :param recursive: to recursively wallk dirs or not
    :return: DirEntry lazy generator of all file entries
    """
    if regex is not None:
        regex = compile(regex) if isinstance(regex, str) else regex
    entries: list[os.DirEntry] = os.scandir(dir_)
    for entry in entries:
        if recursive and entry.is_dir():
            for child in walk_files_in_dir(entry, regex = regex, recursive=recursive):
                if regex is None or regex.match(child.name):
                    yield child
        else:
            if regex is None or regex.match(entry.name):
                yield entry


def print_dir_entry(entry: DirEntry, *, path: bool = False, path_field_size = 70):
    stat = entry.stat()
    kind = 'DIR' if entry.is_dir() else 'FILE'
    data = entry.path if path else entry.name
    print(f"{data:<{path_field_size}s} {kind:<4s} {str(stat.st_size) if entry.is_file() else '':>8s}")


if __name__ == "__main__":
    for entry in walk_files_in_dir(r"D:\CoursePython\python-3.10.2-docs-html", recursive=True, regex=r"^.*\.html$"):
        print_dir_entry(entry, path=True)
    # using walk
    for root, dirs, files in os.walk(r"D:\CoursePython\python-3.10.2-docs-html"):
        for file in files:
            print(file)
