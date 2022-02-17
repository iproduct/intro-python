from typing import Iterable


def body_filter(source_iterator: Iterable[str]) -> Iterable[str]:
    """
    Filter that passes only body of html documents
    :param markup: html or xml markup as Iterable of text lines
    :return: filtered body lines
    """
    pass_through = False
    for line in source_iterator:
        if "<body" in line:
            pass_through = True
        if pass_through:
            yield line


