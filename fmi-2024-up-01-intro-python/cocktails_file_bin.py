import os
import struct

fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
qty = [120.0, 45.84356, 80.0, 95.0, 110.0, 45.334546, 150.0]
global float_size

def trim_zeros(data):
    i = len(bytes) -1
    while i > 0 and data[i] == 0:
        i -= 1
    return data[:i]

if __name__ == '__main__':
    cocktail = list(zip(fruits, qty))
    with open('cocktail.bin', 'wb') as f:
        for ingredient, quantity in cocktail:
            ing_bytes = bytes(ingredient, encoding='utf-8')
            l = len(ing_bytes)
            f.write(ing_bytes + b'0' * (20 - l))
            float_size = struct.pack("f", quantity)
            f.write(bytes())


    print(float_size)
    with open('cocktail.bin', 'rb') as f:
        f.seek(0, os.SEEK_END)
        size = f.tell()
        f.seek(0, os.SEEK_SET)
        while f.tell() < size:
            ing = trim_zeros(f.read(20))
            qty_bytes = f.read(float_size)
            qty = struct.unpack('f', qty_bytes)
