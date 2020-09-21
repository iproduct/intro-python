
def char_count(tree_list):
    if not isinstance(tree_list, list): # recursion bottom
        return len(tree_list)
    sum = 0
    for elem in tree_list:              # recursion step
        sum = sum + char_count(elem)
    return sum

print(char_count([['The', 'instructor'], 'presented',
                  ['wonderful', ['presentation', 'which', 'contained', 'forty', 'sides']],
                  ['in', 'the', 'lecture', 'hall']]))
print(char_count([['The', 'instructor'], 'presented', ['in', 'the', 'lecture', 'hall']]))