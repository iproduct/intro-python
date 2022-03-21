import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting, [ID: %s]", name, threading.get_ident())
    time.sleep(2)
    logging.info("Thread %s: finishing, [ID: %s]", name, threading.get_ident())

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main      : before creating thread")
    th = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main      : thread created")
    th.start()
    logging.info("Main      : waiting thread to finish")
    # th.join()
    logging.info("Main      : all done")