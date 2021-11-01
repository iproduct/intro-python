import re


def f(x):
    return x or "default"

def remove_by_index(l, index):
    """removes element at index position from indexed sequence l and returns the result as new object"""
    return l[:index] + l[index + 1:]

if __name__ == '__main__':
    print(f("hello"))
    print(" | ".join(["Python", "is", "easy"]))
    print(f'Result is {f("hello")}')
    print('Result is: %s' % f("hello"))
    result = f("hello")
    print('Result is: %s, len=%d' % (result, len(result)))
    print('Result is: len = %(length)d, name=%(name)s' % {"name": result, "length": len(result)})
    date_str = "12.07.1982"
    print(re.split("",date_str))
    sum = 0
    for ch in re.split("",date_str):
        sum += int(ch) if ch.isdigit() else 0
    print(sum)
    date_result = date_str[:2] + date_str[3:5] + date_str[6:]
    print(date_result)

    sum = 0
    for ch in date_str:
        if ch != '.':
            sum += int(ch)
    print(f'Sum1 = {sum}')

    digits_list = list(date_str)
    print(digits_list)
    sum = 0
    for ch in digits_list:
        if ch != '.':
            sum += int(ch)
    print(f'Sum2 = {sum}')

    sum = 0
    for ch in date_str:
        sum += int(ch) if ch != '.' else 0
    print(f'Sum3 = {sum}')

    sum = 0
    parts = date_str.split(sep=".")
    print(parts)
    for part in parts:
        for digit in part:
            # print(digit)
            sum += int(digit)
    print(f'Sum4 = {sum}')

    # remove element by remove_by_index
    digits_list = list(date_str)
    print(remove_by_index(digits_list, 3))  # does not mutate original list
    print(digits_list)

    print(digits_list.pop(3))  # mutate original list
    print(digits_list)

    for d in set(date_str):
        print(d)
