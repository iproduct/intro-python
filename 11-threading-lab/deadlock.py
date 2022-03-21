
import threading

if __name__ == "__main__":
    l = threading.Lock()
    print("before first acquire")
    l.acquire()
    print("before second acquire")
    l.acquire()
    print("acquired lock twice")

