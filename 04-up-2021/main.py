import library as mylib

if __name__=="__main__":
    library = mylib.load_from_file("library.csv")
    for book in library:
        book[2] = book[2].split(",")
        book[3] = book[3].split(",")
    print(library)
    mylib.list_by_tags()