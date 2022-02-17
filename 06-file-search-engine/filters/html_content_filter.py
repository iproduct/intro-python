from typing import Iterable


def html_content_filter(source_iterator: Iterable[str]) -> Iterable[str]:
    for line in source_iterator:
        line = line.strip()
        if len(line) > 0:
            yield line[:80]
