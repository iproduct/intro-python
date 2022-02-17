import os

if __name__ == '__main__':
    # list_of_dir_entries = os.listdir(r"D:\CoursePython\python-3.10.2-docs-html")
    list_of_dir_entries = os.scandir(r"D:\CoursePython\python-3.10.2-docs-html")
    entry: os.DirEntry
    for entry in list_of_dir_entries:
        stat = entry.stat()
        kind = 'DIR' if entry.is_dir() else 'FILE'
        print(f"{entry.name:<30s} {kind:<4s} {str(stat.st_size) if entry.is_file() else '':>8s}")