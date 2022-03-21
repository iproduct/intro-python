import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, Future


def task(data):
    n, p = data
    logging.info("Thread %s: starting, [ID: %s]", n, threading.get_ident())
    time.sleep(n)
    res = 1
    for i in range(p):
        res *= n
    logging.info("Thread %s: finishing, [ID: %s]", n, threading.get_ident())
    return res

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with ThreadPoolExecutor(max_workers=3) as executor:
        problems = [(10, 125), (5, 10), (9, 137), (4, 42), (2, 5)]
        responses = executor.map(task, problems);

    for resp in responses:
        logging.info("Thread result: %s: [ID: %s]", resp, threading.get_ident())
