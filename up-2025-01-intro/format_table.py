users = [
    (1, 'Ivan', 'Petrov', 28, 'Sofia', '08871234567', '2021-04-15'),
    (2, 'Dimitar', 'Ivanov', 28, 'Plovdiv', '0886786787686', '2023-01-30'),
    (3, 'Violeta', 'Blagoeva', 28, 'Varna', '08897654321', '2024-03-12'),
    (4, 'Hrisitna', 'Petrova', 28, 'Haskovo', '08996543218', '2024-11-05'),
    (5, 'Hristo', 'Yankov', 28, 'Ruse', '08764235667', '2025-01-30')
]

columns = ('No', 'Name', 'Family', 'Age', 'City', 'Phone', 'Date')

def format_table(columns: tuple[str], data: list[tuple[str|int]]) -> str:
    # TODO 1) claculate the width of each column
    all_data = [columns]
    all_data.extend(data)
    print(all_data)
    lengths = []
    for col in range(len(all_data[0])): # for each column
        maxlen = 0
        for row in range(len(all_data)):   # for each row in a column
            cell_data_len = len(str(all_data[row][col])) # calculate length of the string in the table cell
            if cell_data_len > maxlen:     #find maximum length of the string in the table cell
                maxlen = cell_data_len
        lengths.append(maxlen)
    print('Max lengths of columns:', lengths)

    # TODO 2) print first row with column labels
    result = '|'
    for col in range(len(columns)):
        result += f' {columns[col].center(lengths[col])} |'

    # TODO 3) print next rows with data
    for row in range(len(data)):
        result += '\n|'
        for col in range(len(columns)):
            if type(data[row][col]) == str:
                result += f' {str(data[row][col]).ljust(lengths[col])} |'
            else:
                result += f' {str(data[row][col]).rjust(lengths[col])} |'

    result += '\n'
    return result


if __name__ == "__main__":
    print(users)
    print(format_table(columns, users))