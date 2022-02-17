from typing import Iterable


def html_content_filter(source_iterator: Iterable[str]) -> Iterable[str]:
    """
    Filter out markup from document using line Iterables
    :param markup: html or xml markup as Iterable of text lines
    :return: filtered plain text (content only without tags) as Iterable of content lines
    """
    for line in source_iterator:
        content = ""
        start = 0
        end = -1
        # print(line)
        # while start >= 0:
        #     start = line.find("<", end  + 1)
        #     if start < 0:
        #         content += line[end + 1:]
        #     else:
        #         content += line[end + 1:start]
        #         end = line.find(">", start + 1)
        #         if end < 0:
        #             break
        # content = content.strip()
        # if len(content) > 0:
        #     yield content
        yield line


