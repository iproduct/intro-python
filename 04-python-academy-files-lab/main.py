
def compare_str_ignore_case(s: str) -> str:
    return s.lower()
    # return str.lower(s)

if __name__ == '__main__':
    l = ['Orange', 'orange', 'banana', 'kiwi', 'mango', 'pineapple']
    l.sort(key=compare_str_ignore_case)
    print(l)

    books = [
        (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
        (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
        (3, "Python Crash Course, 2nd Edition", "A Hands-On, Project-Based Introduction to Programming", "Eric Matthes", "No Starch Press", 2014, 9.56),
        (4, "Python Pocket Reference", "Python in Your Pocket", "Mark Lutz", "O'Reily", 2002, 9.4),
        (5, "Python for Data Analysis", "Data Wrangling with Pandas, NumPy, and IPython", "Wes Mckinney", "O'Reily", 2017, 30.75),
        (6, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011,
         135.9)
    ]


