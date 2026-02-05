from typing import Iterable, Any


def print_as_table(data: Iterable[Iterable[Any]], /, width, *, alignment='left', **kwopts) -> None:
    # print(options, type(options))
    print(kwopts, type(kwopts))
    # width = options[0]
    column_sep = kwopts.get('column_sep', '|')
    capitalize = kwopts.get('capitalize', None)
    for row in data:
        print(column_sep, end='')
        for column in row:
            val = str(column)
            if capitalize == "upper":
                val = val.upper()
            if alignment == "left":
                print(val.ljust(width), column_sep, sep='', end='')
            elif alignment == "right":
                print(val.rjust(width), column_sep, sep='', end='')
            else:
                print(val.center(width), column_sep, sep='', end='')
        print()


if __name__ == "__main__":
    phones = [
        ['Trayan', 'Iliev', '0876123456'],
        ['Samuil', 'Petrov', '0986123456'],
        ['Georgi', 'Hristov', '0865433333'],
        ['Tatiana', 'Ivanova', '0898765432'],
        ['Petar', 'Petrov', '0892877654'],
    ]
    print_as_table(phones, 10)
    print_as_table(phones, 12, alignment='center', column_sep='!', capitalize='upper')