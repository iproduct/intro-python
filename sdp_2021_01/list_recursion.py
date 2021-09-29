l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def print_list_recursive(l):
    if len(l) == 0:
        return
    print(l[0]) # print head
    print_list_recursive(l[1:]) # process tail recursive

if __name__ == '__main__':
    print_list_recursive(l)