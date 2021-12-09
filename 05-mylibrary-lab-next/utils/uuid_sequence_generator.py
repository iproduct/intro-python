import uuid

def uuid_sequence_generator():
    while True:
        yield str(uuid.uuid1())

def fib_generator():
    a, b = 0 ,1
    while True:
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    # fib_gen = fib_generator()
    # for fib in (next(fib_gen) for x in range(0, 20)):
    #     print(fib)

    id_gen = uuid_sequence_generator()
    for fib in (next(id_gen) for x in range(0, 10)):
        print(fib)