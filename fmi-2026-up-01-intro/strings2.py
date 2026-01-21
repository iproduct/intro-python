
if __name__ == '__main__':
    # s = '\u23F0' * 40
    s = '\U0001F4D6' * 40
    print(s)

    coord = [3, 5]
    print('X: {0[0]};  Y: {0[1]}'.format(coord, 'Hi'))
    print('X: {0};  Y: {1}'.format(*coord))

    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print('Coordinates: {0[latitude]}, {0[longitude]}'.format(coord))
    print('Coordinates: {latitude}, {longitude}'.format(**coord))

