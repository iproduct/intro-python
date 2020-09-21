"""This module demonstrates usage of if-else statements, while loop and break."""

def calculate_grade(grade):
    """Function that calculates final grades based on points earned."""
    if grade >= 90:
        if grade == 100:
            return 'A+'
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    return 'F'

if __name__ == '__main__':
    while True:
        grade_str = input('Number of points (<ENTER> for END): ')
        if len(grade_str) == 0:
            break
        points = int(grade_str)
        print(calculate_grade(points))
    print('Good Bye!')
