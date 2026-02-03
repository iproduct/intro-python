
# return lines with line numbers prepended
def enumerate_lines(filename):
    result_lines = []
    with open(filename, 'rt', encoding='utf-8') as f: # recommended way to open a file with auto closing
        for i, line in enumerate(f, start=1):
            result_lines.append(str(i) + ': ' + line.rstrip()) # remove /n at the line end
    return result_lines

def get_comments(filename):
    result_lines = []
    with (open(filename, 'rt', encoding='utf-8') as f):  # recommended way to open a file with auto closing
        for line in f:
            line = line.rstrip() # remove new line at the line end
            index = line.find('#') # check if there is single line comment
            while index != -1 and is_in_python_string(line, index):
                index = line.find('#', index + 1)
            if index != -1:
                result_lines.append(line[index:]) # get comment only
    return result_lines

str_begins = {'\'', '"', '"""', "'''"}
def is_in_python_string(line, index):
    instr = False
    for i in range(index + 1, len(line)):
        if not instr:
            for str_begin in str_begins:
                if line[i: i+ len(str_begin)] == str_begin:
                    if i == 0 or (i > 0 and line[i - 1] != '\\'):
                        instr = True
                        begin = str_begin
                        break
        else:
            if line[i: i + len(begin)] == begin:
                instr = False
    return instr


# Test the demo
if __name__ == '__main__':
    for line in get_comments('enumerate_lines.py'):
        print(line)

    # print(is_in_python_string("            index = line.find('#') #check if there is single line comment", 30))