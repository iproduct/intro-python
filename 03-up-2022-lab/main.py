import sys

if __name__ == '__main__':
    f = open("out.txt", "wt")
    print("abc", "def", "hello", "Python", sep=" | ", end=" | ", file=f, flush=True)
    print("abc", "def", "hello", "Python", sep=" | ", end=" | ", file=f)
    print("abc", "def", "hello", "Python", sep=" | ", end=" | ", file=f)
    f.close()
