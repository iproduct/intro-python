def get_python_module_stat(module_file_path):
    classes = 0
    functions = 0
    with open(module_file_path, 'rt') as f:
        for line in f:
            words = line.strip().split(' ')
            for word in words:
                if word == 'class':
                    classes += 1
                if word == 'def':
                    functions += 1
    return {'classes': classes, 'functions': functions}

if __name__ == '__main__':
    print(get_python_module_stat('file_iterator.py'))