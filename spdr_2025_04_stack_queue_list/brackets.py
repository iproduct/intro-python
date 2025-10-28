import string
from collections import deque

bracket_correspondence_map = {'(': ')', '{': '}', '[': ']'}

def are_brackets_correct(expression: str) -> (bool, int):
    stack = deque()
    for index, char in enumerate(expression):
        if char in bracket_correspondence_map: #check for opening bracket
            stack.append(char)
            print('-> ', char, " : ", stack)
        else:
            if len(stack) == 0: return False, index
            last_bracket = stack.pop()
            print('<- ', last_bracket, " : ", stack)
            if bracket_correspondence_map[last_bracket] != char:
                return False, index
    return len(stack) == 0, len(expression)

if __name__ == '__main__':
    print(are_brackets_correct("}(}{([])}){}"))