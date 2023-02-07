product_type = tuple[str, float]
def input_product() -> product_type:
    """
    Inputs a product from command line
    :return: a tuple of product name and quantity
    """
    product_name = input('Product name (empty for end):').strip()
    if len(product_name) == 0:
        return None
    qty = float(input('Quantity:').strip())
    return (product_name, qty)

def input_product_list() -> list[product_type]:
    products = []
    finished = False
    while not finished:
        product = input_product()
        if product is None:
            finished = True
        else:
            products.append(product)
    return products


def stringify_product(product: product_type) -> str:
    return f'{product[0]:<15s} -> {product[1]:7.2f}\n'

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
    print(product_prices)
    products = input_product_list()
    save_product_list(products)
    print('Shopping saved succesfully')