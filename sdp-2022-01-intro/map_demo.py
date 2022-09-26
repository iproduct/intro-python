def starts_with_a(name: str) -> bool:
    return name.lower().startswith('a')

if __name__ == '__main__':
    predicate = starts_with_a
    fruits = ['Orange', 'Apple', 'Pineapple', 'Banana', 'Apricot']
    print(list(map(str.lower, filter(lambda fruit: fruit.lower().startswith('a'), fruits))))