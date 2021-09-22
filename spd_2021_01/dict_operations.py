
if __name__ == '__main__':
    grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
    print( list(enumerate(dict.keys(grades))) )
    print( [k[1] for k in enumerate(dict.keys(grades))] )
    print( [k for _, k in enumerate(dict.keys(grades))] )
    print( tuple(dict.values(grades)) )
    print( list(dict.items(grades)) )
    print( {k for k, v in dict.items(grades)} )
    print( [v for k, v in dict.items(grades)] )