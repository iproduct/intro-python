max_number = 1000

if __name__ == '__main__':
    numbers = list(range(2,max_number + 1))
    next = 0
    while next < len(numbers):
        chosen = numbers[next]
        for i in range(2 * chosen, len(numbers) + 2, chosen):
            numbers[i - 2] = 0
        next += 1
        while next < len(numbers) and not numbers[next] :
            next += 1
    print(numbers)

    for i in range(max_number + 1):
        if numbers[i]:
            print(i + 2, end=", ")
