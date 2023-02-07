product_type = tuple[str, float] # product name and price
purchase_type = tuple[str, float, float] # product name, price, and quantity

def print_products_menu(product_prices: list[product_type]):
    for index, product_price in enumerate(product_prices):
        print(f'{index + 1}: {product_price[0]}')

def input_product(product_prices: list[product_type]) -> purchase_type:
    """
    Inputs a product from command line
    :return: a tuple of product name and quantity
    """
    print_products_menu(product_prices)
    answer = input('Select product index (empty for exit):').strip()
    if len(answer) == 0:
        return None
    index = int(answer) - 1
    product_price = product_prices[index]
    name = product_price[0]
    price = product_price[1]
    qty = float(input(f'{name} [{price} lv] quantity:').strip())
    return (name, price, qty)

def input_product_list(product_prices: list[product_type]) -> list[product_type]:
    products = []
    finished = False
    while not finished:
        product = input_product(product_prices)
        if product is None:
            finished = True
        else:
            products.append(product)
    return products


def stringify_product(product: purchase_type) -> str:
    return f'{product[0]:<15s} [{product[1]:6.2f}] -> {product[2]:7.2f} | {product[1] * product[2]:7.2f}\n'

def save_product_list(products: list[product_type]):
    product_strings = map(stringify_product, products)
    with open('shoping_list.txt', 'wt', encoding='utf-8') as f:
        f.writelines(product_strings)

def load_product_prices(filename: str) -> list[product_type]:
    results = []
    with open(filename, 'rt', encoding='utf-8') as f:
        for line in f:
            name_and_price_list = line.strip().split(',')
            results.append((name_and_price_list[0].strip(), float(name_and_price_list[1].strip())))
    return results


if __name__ == '__main__':
    product_prices = load_product_prices('product_prices.csv')
    # print(product_prices)
    products = input_product_list(product_prices)
    save_product_list(products)
    print('Shopping saved succesfully')