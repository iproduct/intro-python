from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())

