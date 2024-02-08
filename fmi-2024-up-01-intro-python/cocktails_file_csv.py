fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
qty = [120, 45.84356, 80, 95, 110, 45.334546, 150]

if __name__ == '__main__':
    cocktail = zip(fruits, qty)
    with open('cocktail.csv', 'wt', encoding='utf-8') as f:
        f.write('Ingredient,Qty\n')
        for ingredient, quantity in cocktail:
            f.write(f'{ingredient},{quantity}\n')