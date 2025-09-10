def hanoy_towers(num_disks: int, begin: int, end: int) -> None:
    if num_disks == 0: #recursion bottom
        return
    else:              #recursion step
        intermediary = 6 - begin - end
        hanoy_towers(num_disks - 1, begin, intermediary)
        print(f'Move DISK{num_disks} from {begin} to {end}')
        hanoy_towers(num_disks - 1, intermediary, end)

if __name__ == '__main__':
    hanoy_towers(4, 1, 3)