if __name__ == "__main__":
    d = dict()
    d2 = {}
    print(type(d2))
    s = set()
    print(type(s))
    d3 = dict([('name', 'Trayan'), ('course', 'UP')])
    print(d3)
    ingredients = ['tequila', 'rom', 'orange juice', 'lemon', 'menta', 'tomato', 'vodka']
    quantities = [50, 20, 0, 15, 0, 0, 0]
    print(dict(zip(ingredients, quantities)))
    d3.setdefault()