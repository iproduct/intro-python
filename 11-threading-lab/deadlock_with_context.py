import threading

if __name__ == "__main__":
    with threading.Lock() as l:
        print("before first acquire")
    print("after first acquire")
    with threading.Lock() as l:
        print("acquired lock twice")
    print("after second acquire")