fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
qty = [120, 45.84356, 80, 95, 110, 45.334546, 150]

if __name__ == '__main__':
    cocktail = zip(fruits, qty)
    with open('cocktail.txt', 'wt', encoding='utf-8') as f:
        f.write(f'{"Ingredient":^12s} {"Qty":^7s}\n')
        f.write(f'{"-" * 20}\n')
        for ingredient, quantity in cocktail:
            f.write(f'{ingredient:<12s} {quantity:>7.2f}\n')