

def is_plindrom(string):
    string = string.replace(" ", "")
    n = len(string)
    stack = []
    for char in string[:n//2]:
        stack.append(char)
    for char in string[(n+1)//2:]:
        print(char, stack[-1])
        if stack.pop() != char:
            return False
    return True

if __name__ == '__main__':
    print(is_plindrom("бял хляб"))