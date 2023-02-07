def filter(filtered_list: list[str], filter_str: str) -> list[str]:
    result = []
    for s in filtered_list:
        if s.lower().find(filter_str) >= 0:
            result.append(s)
    return result

if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
    qty = [120, 45.84356, 80, 95, 110, 45.334546, 150]
    fruits_qty = dict(zip(fruits, qty))
    print(fruits_qty)
    # s = ' | '.join(l)
    # print(filter(l, 'an'));

    print('Cocktail Recipe:')
    sum = 0
    for fruit in fruits_qty:
        qty = fruits_qty[fruit]
        # print(f'{fruit:10} -> {qty[index]:6.2f}')
        # print('%-10s -> %6.2f' % (fruit, qty))
        print('{0:^10s} -> {1:6.2f}'.format(fruit, qty))
        sum += qty
    print('-' * 20)
    print(f'{"Total":10} -> {sum:6.2f}')
    print('\n')
    print(fruits[3][-7:-1:2])