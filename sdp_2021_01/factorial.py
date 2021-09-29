def fact(n: int) -> int:
    """fact(n) подразбира че n е
положително цяло число и връща като
резултат числото n! """
    if n == 1:
        # print('recursion bottom')
        return 1  # botom
    else:
        # print(f'-> {n} * fact({n-1})')
        result = n * fact(n - 1)  # step
        # print(f'<- {n} * fact({n - 1}) : {result}')
        return result


if __name__ == '__main__':
    input_filen_name = 'factorial_input.txt';
    with open(input_filen_name, 'rt') as input_file:
        n_str = input_file.readline()
        try:
            n = int(n_str)
        except ValueError:
            print(f'Error: The file {input_filen_name} contains invalid data for N: {n_str}')
            exit(1)

    with open('factorial_results.txt', 'wt') as f:
        # f.seek(0, 2)
        for i in range(1, n + 1):
            print(i, fact(i), sep=',', end='\n', file=f)
