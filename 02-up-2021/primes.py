import math

max_number = 1000

if __name__ == '__main__':
    # numbers = list(range(2, max_number + 1))
    numbers = [True] * (max_number - 2)
    # print(numbers)
    next = 0
    upper_bound = int(math.sqrt(max_number))
    while next < upper_bound:
        chosen = next + 2
        # zero all multiples of chosen
        for i in range(2 * chosen, len(numbers) + 1, chosen):
            numbers[i - 2] = False
        next += 1
        # find first non-ziroed index
        while next < len(numbers) and not numbers[next] :
            next += 1

    # print(numbers)

    for i in range(max_number - 2):
        if numbers[i]:
            print(i + 2, end=", ")
            # print(numbers[i], end=", ")
