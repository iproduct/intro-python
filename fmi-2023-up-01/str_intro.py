def filter(filtered_list: list[str], filter_str: str) -> list[str]:
    result = []
    for s in filtered_list:
        if s.lower().find(filter_str) >= 0:
            result.append(s)
    return result

if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Kiwi', 'Pineapple', 'Orange', 'Cherry', 'Grape']
    qty = [120, 45.84356, 80, 95, 110, 45.334546, 150]
    # s = ' | '.join(l)
    # print(filter(l, 'an'));

    print('Cocktail Recipe:')
    sum = 0
    for (index, fruit) in enumerate(fruits):
        print(f'{fruit:10} -> {qty[index]:6.2f}')
        sum += qty[index]
    print('-' * 20)
    print(f'{"Total":10} -> {sum:6.2f}')