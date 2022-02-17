from files.file_walker import walk_files_in_dir, print_dir_entry
from filters.html_content_filter import html_content_filter
from reducers.word_count import word_count_reducer

if __name__ == '__main__':
    max_files = 200
    count = 0
    for entry in walk_files_in_dir(r"D:\CoursePython\python-3.10.2-docs-html\tutorial", recursive=True, regex=r"^.*\.html$"):
        # print_dir_entry(entry, path=True)
        if count >= max_files:
            break;
        count += 3
        print("\n\nFILE:", entry.path)
        with open(entry.path, "rt", encoding="utf-8") as f:
            # print(f.read())
            word_counts = word_count_reducer(html_content_filter(f))
            # for content_line in html_content_filter(f):
            #     print(word_counts)
            for item in word_counts:
                print(f"{item[0]:20s} -> {item[1]:3d}")


