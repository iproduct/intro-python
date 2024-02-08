import os
import struct

fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
qty = [120.0, 45.84356, 80.0, 95.0, 110.0, 45.334546, 150.0]
INGREDIENT_SIZE = 20
QUANTITY_SIZE = 4
RECORD_SIZE = INGREDIENT_SIZE + QUANTITY_SIZE

def trim_zeros(data):
    i = len(data) -1
    while i > 0 and data[i] == 0:
        i -= 1
    return data[:i+1]


def read_record(f):
    ing = trim_zeros(f.read(20)).decode("utf-8")
    qty_bytes = f.read(QUANTITY_SIZE)
    qty, = struct.unpack('f', qty_bytes)
    return ing, qty

if __name__ == '__main__':
    cocktail = list(zip(fruits, qty))
    with open('cocktail.bin', 'wb') as f:
        for ingredient, quantity in cocktail:
            ing_bytes = bytes(ingredient, encoding='utf-8')
            l = len(ing_bytes)
            f.write(ing_bytes + b'\x00' * (INGREDIENT_SIZE - l))
            qty_bytes = struct.pack("f", quantity)
            f.write(qty_bytes)

    with open('cocktail.bin', 'rb') as f:
        f.seek(0, os.SEEK_END)
        size = f.tell()
        f.seek(0, os.SEEK_SET)
        while f.tell() < size:
            ing, qty = read_record(f)
            print(ing, qty)

        f.seek(4 * RECORD_SIZE, os.SEEK_SET)
        ing, qty = read_record(f)
        print("\n5-th record:\n", ing, qty)