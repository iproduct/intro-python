from files.file_walker import walk_files_in_dir, print_dir_entry
from filters.html_content_filter import html_content_filter

if __name__ == '__main__':
    max_files = 3
    count = 0
    for entry in walk_files_in_dir(r"D:\CoursePython\python-3.10.2-docs-html", recursive=True, regex=r"^.*\.html$"):
        # print_dir_entry(entry, path=True)
        if count >= max_files:
            break;
        count += 1
        with open(entry.path, "rt", encoding="utf-8") as f:
            for content_line in html_content_filter(f):
                print(content_line)

