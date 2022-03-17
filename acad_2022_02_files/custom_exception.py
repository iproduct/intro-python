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
            raise #MyException("Risen from except clause: " + str(ex)) from ex
    except Exception as ex:
        ex_info = sys.exc_info()
        print("Catched:", ex, ", Exc. info:", ex_info, ":")
        traceback.print_tb(ex_info[2], file=sys.stdout)
        summary = traceback.StackSummary.extract(traceback.walk_tb(ex_info[2]))
        print(">>>", summary)


    print("Program contounes normally.")