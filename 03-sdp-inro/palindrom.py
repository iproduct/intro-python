def is_palindrom(str):
    if len(str) <= 1:
        return True
    if str[0].lower() == str[-1].lower():
        return is_palindrom(str[1: -1])
    return False

def remove_spaces(str):
    result = ''
    for ch in str:
        if ch != ' ':
            result = result + ch
    return result

s1 = 'Able was I ere I saw Elba'
s2 = 'Are we not drawn onward we few drawn onward to new era'

s3 = 'Are we not drawn onward, we few, drawn onward to new era?'

print(f'{s1}: {is_palindrom(s1)}')
print(f'{s2}: {is_palindrom(remove_spaces(s2))}')
print(f'{s3}: {is_palindrom(remove_spaces(s3))}')