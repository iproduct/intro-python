""" Extracting Python comments """


def enumerate_lines(filename):
    """ Prepends lines with line numbers
    :param filename: the name of the text file to read from
    :return: a list of lines in input file prepended with a line number
    """

    result_lines = []
    with open(filename, 'rt', encoding='utf-8') as f: # recommended way to open a file with auto closing
        for i, line in enumerate(f, start=1):
            result_lines.append(str(i) + ': ' + line.rstrip()) # remove /n at the line end
    return result_lines


def get_comments(filename):
    """ Returns a list of Python single line comments starting with '#'
    :param filename: the name of the text file to read from
    :return: a list of single line comments in the input file
    """
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
    """ Returns True if the character at index 'index' is in a python string
    :param line: the line to check
    :param index: the index to check
    :return: True if the character at index 'index' is in a python string"""
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

def write_to_file(filename, lines):
    """ Writes lines to a text file
    :param filename: the name of the text file to write to
    :param lines: the lines to write
    """
    with open(filename, 'wt', encoding='utf-8') as f:
        for line in lines:
            f.write(line+"\n")


# Test the demo
if __name__ == '__main__':
    comments = get_comments('enumerate_lines.py')
    for line in comments:
        print(line)
    write_to_file('comments.txt', comments)