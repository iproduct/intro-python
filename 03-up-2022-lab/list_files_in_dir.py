import os
import re
from typing import Iterable


def list_files_in_dir(dir_: str = '.', *, regex=None, recursive=False) -> Iterable[os.DirEntry]:
    if regex is not None:
        regex = re.compile(regex) if isinstance(regex, str) else regex
    entries = os.scandir(dir_)
    for entry in entries:
        if recursive and entry.is_dir():
            for child in list_files_in_dir(entry, regex = regex, recursive = recursive):
                yield child
        else:
            if regex is None or regex.match(entry.name):
                yield entry


if __name__ == "__main__":
    for entry in list_files_in_dir(recursive=True):
        print(f"{entry.path:80s} {'<DIR>' if entry.is_dir() else str(entry.stat().st_size):>10s}")
