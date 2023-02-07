if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
    qty = [120, 45.84356, 80, 95, 110, 45.334546, 150]
    fruits_qty = dict(zip(fruits, qty))

    with open('coctail.txt', 'wt', encoding="utf-8") as f:
        f.write('Cocktail Recipe:\n')
        f.write('-' * 20 + '\n')
        sum = 0
        for fruit in fruits_qty:
            qty = fruits_qty[fruit]
            f.write('{0:<10s} -> {1:6.2f}\n'.format(fruit, qty))
            sum += qty
        f.write('-' * 20+'\n')
        f.write(f'{"Total":10} -> {sum:6.2f}\n')