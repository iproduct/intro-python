import logging
import threading
import time
import concurrent.futures


def thread_function(name):
    logging.info("Thread %s: starting, [ID: %s]", name, threading.get_ident())
    time.sleep(2)
    logging.info("Thread %s: finishing [ID: %s]", name, threading.get_ident())
    return f"Result {name}"


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(thread_function, range(3))

    for index, result in enumerate(results):
        logging.info("Main    : thread %d done with result: %s", index, result)
