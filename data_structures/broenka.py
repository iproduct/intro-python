def find_winner(n: int, m: int) -> int:
    participants = [i for i in range(1, n+1)]
    print(f'Initial participants: {participants}')
    current = 0
    length = n
    while length > 1:
        current = (current + m - 1) % length
        removed = participants.pop(current)
        print(f'Removing participant {removed}, remaining: {participants}')
        length -= 1
    return participants[0]

if __name__ == '__main__':
    print(f'Winner: {find_winner(11, 5)}')