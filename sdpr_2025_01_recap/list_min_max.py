def find_min_max_index(l: list) -> (int, int):
    min = l[0]
    min_index = 0
    max = l[0]
    max_index = 0
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
            min_index = i
        if l[i] > max:
            max = l[i]
            max_index = i
    return min_index, max_index

def get_max_count(l: list) -> int:
    max = l[0]
    count = 1
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
            count = 1
        elif l[i] == max:
            count += 1
    return count

if __name__ == '__main__':
    l = [42, 92, 2, 12, 17, 92, 8, 9, 4, 18, 2, 7, 45, 92, 7, 5]
    min_index, max_index = find_min_max_index(l)
    print(f'Min l[{min_index}] = {l[min_index]}, Max l[{max_index}] = {l[max_index]}')
    print(f'Max count = {get_max_count(l)}')

