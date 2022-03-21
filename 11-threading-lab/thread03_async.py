import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, Future


def future_callback(f: Future[int]):
    res = f.result()
    logging.info("Thread finished with result: %s: [ID: %s]", res, threading.get_ident())

def task(n, p):
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

    with ThreadPoolExecutor(max_workers=5) as executor:
        problems = [(10, 125), (5, 10), (9, 137), (4, 42), (2, 5)]
        future_res = []
        for problem in problems:
            future_res.append(executor.submit(task, *problem));
        for i, fr in enumerate(future_res):
            fr.add_done_callback(future_callback)
    # executor.shutdown(wait=True, cancel_futures=True)
