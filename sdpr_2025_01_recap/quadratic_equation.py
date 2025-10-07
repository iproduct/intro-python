
if __name__ == '__main__':
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            break
        except ValueError:
            print("Please enter numbers only. Tray again")
    print(f'a = {a}, b = {b}, c = {c}')