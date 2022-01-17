import sys


class MyException(Exception):
    def __init__(self, *args):
        # Exception.__init__(self, *args)
        super().__init__(*args)


def erroneuos():
    try:
        return 1 / 0
    except:
        print("Within except.")
        raise
    finally:
        print("Within finally.")

if __name__ == "__main__":
    try:
        erroneuos()
    except Exception as ex:
        # tb = sys.exc_info()[2]
        # print(f"Type: {sys.exc_info()[0]}, Value: {sys.exc_info()[1]}\n")
        raise MyException("Raised from main()") from ex
