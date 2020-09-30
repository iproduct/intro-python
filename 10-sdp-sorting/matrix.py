from random import randint

def array_2d_str(matrix):
    result = ''
    for i in range(len(matrix)):
        line = ''
        for j in range(len(matrix[i])):
            line += str(matrix[i][j]) + ', '
        result += line  + '\n'
    return result

if __name__ == '__main__':
    # 2D array = matrix
    # m = [[0] * 10] * 5
    m = [[randint(1, 100) for i in range(10)] for j in range(5)]
    print(array_2d_str(m))
