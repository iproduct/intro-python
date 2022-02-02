def get_primes(n):
    results = []
    nums = [i + 2 for i in range(n-1)]
    i = 0
    while i < n - 1:
        # find first nonzero number
        while i < n - 1 and nums[i] == 0:
            i += 1
        if i < n - 1:
            p = nums[i]
            print(p)
            results.append(p)
            # zero all numbers dividable by p
            j = i
            while j < n - 1:
                nums[j] = 0
                j += p
            i += 1
    return results

if __name__ == '__main__':
    n = int(input("Input N:"))
    print(get_primes(n))