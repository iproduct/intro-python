text = [
    'A New Beginning In Your Life',
    'Development, cooperation, and waiting',
    'Social expansion and creative successes',
    'Hard work and slow, but steady progress',
    'Feeling Loose and Free',
    'Love, Family, Home and Responsibility',
    'a time for analysis and understanding',
    'Attainment and capital gains',
    'Reflection and Reaching Out'
]


if __name__ == '__main__':
    s = 'Hello world!'
    print(s[::-1])
    date = input("Birth date:")
    while len(date) > 1:
        sum = 0
        for ch in date:
            if ch.isdigit():
               sum += int(ch)
        print(sum)
        date = str(sum)
    print(f'You number is: {date}')
    print(text[sum - 1])
