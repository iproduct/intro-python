
def hanoi(n, from_tower, to_tower, other_tower):
    if n == 1: # recursion bottom
        print(f'{from_tower} -> {to_tower}')
    else:      # recursion step
        hanoi(n - 1, from_tower, other_tower, to_tower)
        print(f'{from_tower} -> {to_tower}')
        hanoi(n - 1, other_tower, to_tower, from_tower)

hanoi(4, 1, 3, 2)
