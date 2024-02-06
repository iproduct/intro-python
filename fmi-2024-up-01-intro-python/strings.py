if __name__ == '__main__':
    s = 'Hello Python from python and Python.'
    for i, ch in enumerate(s):
        print(i, ': ', ch, ' -> ', ord(ch))

    gps_pos = {'latitude': '32.24N', 'longitude': '-115.81W'}
    print("(Lat: {0[latitude]}, Lon: {0[longitude]})".format(gps_pos))
    print("(Lat: {latitude}, Lon: {longitude})".format(**gps_pos))

    b = 'Hello'.encode('utf-8')
    print(list(b), type(b))
    s2 = b.decode('utf-8')
    print(list(s2), type(s2))

    query = 'python'
    ls = s.lower()
    pos = ls.find(query, 0)
    while pos > 0:
        print(f"Found '{s[pos : pos + len(query)]}' at pos: {pos}")
        pos = ls.find(query, pos + 1)