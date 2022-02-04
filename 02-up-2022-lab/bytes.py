if __name__ == '__main__':
    s = "abя"
    # b = bytes(s, encoding='utf-8')
    b = s.encode(encoding="utf-8")
    print(list(s))
    print(list(b))
    print(b)
    # r = str(b[2:], encoding="utf-8")
    r = b[2:].decode(encoding="utf-8")
    print(r, type(r))

    ba = bytearray(b)
    ba[0] += 3
    ba.append(97)
    print(ba, len(ba))

    sba = ba.decode(encoding="utf-8")
    print(sba, len(sba))