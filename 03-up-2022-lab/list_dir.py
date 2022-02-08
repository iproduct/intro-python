import os, fnmatch

if __name__ == '__main__':
    # listOfFiles = os.listdir()
    listOfDirEntry = os.scandir()
    pattern = "*.py"
    for entry in listOfDirEntry:
        # if fnmatch.fnmatch(entry, pattern):
        print (entry.name, "DIR" if entry.is_dir() else "FILE")