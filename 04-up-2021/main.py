# import library
# import library as mylib
from library import list_by_tags, load_from_file

if __name__=="__main__":
    library = load_from_file("library.csv")
    for book in library:
        book[2] = book[2].split(",")
        book[3] = book[3].split(",")
    print(library)
    list_by_tags(library)