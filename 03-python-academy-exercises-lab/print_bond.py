books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 135.9)
]

def print_bond(items):
    result = ""
    sum = 0
    for b in items:
        # result += "| {:^3d} | {:<15.15s} | {:<15.15s} | {:<20.20s} | {:^12.12s} | {:<4d} | {:>7.2f} |\n"\
        #     .format(*b)
        line = f"| {b[0]:^3d} | {b[1]:<15.15s} | {b[2]:<15.15s} | {b[3]:<20.20s} | {b[4]:^12.12s} | {b[5]:<4d} | {b[6]:>7.2f} |\n"
        result += line
        sum += b[-1]
    l = len(line)
    total_str = f"Total: {sum:8.2f}  \n"
    prefix = " " * (l - len(total_str))
    result += prefix + total_str
    result += prefix + f"VAT  : {sum:8.2f}  \n"
    return result

if __name__ == '__main__':
    print(print_bond(books))