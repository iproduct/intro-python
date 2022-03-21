
import threading
import time

l = threading.RLock()

def util():
    l.acquire()
    print("In util(): acquired lock in util")
    time.sleep(1)
    print("In util(): releasing lock in util")
    l.release()


if __name__ == "__main__":
    # calling with lock acquired
    print("acquiring lock in main()")
    l.acquire()
    print("before calling util() function")
    util()
    print("after returning from util() function")
    l.release()
    print("released lock in main()")

    # calling without lock
    print("before calling util() function")
    util()
    print("after returning from util() function")


