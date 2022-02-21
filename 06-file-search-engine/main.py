import os
import sys

import pipeline
from files.file_walker import walk_files_in_dir
from pipeline import body_filter, html_content_filter, word_count_reducer

# from pipeline.filters.html_content_filter import html_content_filter
from pipeline.reducers.word_count import word_count_reducer

if __name__ == '__main__':
    print(sys.path)
    print(dir(pipeline.reducers.word_count))
    max_files = 1
    count = 0
    for entry in walk_files_in_dir(r"D:\CoursePython\python-3.10.2-docs-html", recursive=True, regex=r"^.*\.html$"):
        if count >= max_files:
            break
        count += 1
        print("\n\nFILE:", entry.path)
        with open(entry.path, "rt", encoding="utf-8") as f:
            # word_counts = html_content_filter(body_filter(f))
            # for line in word_counts:
            #     print(line)
            word_counts = word_count_reducer(
                html_content_filter(
                    body_filter(f)), max_keywords=20)
            for item in word_counts:
                print(f"{item[0]:20s} -> {item[1]:3d}")

    # os.system("start " + entry.path)
