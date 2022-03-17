import sys
import traceback


class MyException(Exception):
    pass


def erroneous():
    try:
        return 1 / 0
    except Exception as ex:
        print("Exception catched.", ex, type(ex))
        raise
    finally:
        print("In finally clause - cleaning up.")


if __name__ == "__main__":
    try:
        try:
            erroneous()
        except Exception as ex:
            raise MyException("Risen from except clause: " + str(ex)) from ex
    except MyException as ex:
        exinfo = sys.exc_info()
        print("Catched:", ex, ", Exc. info:")
        traceback.print_tb(exinfo[2], file=sys.stdout)


    print("Program contounes normally.")