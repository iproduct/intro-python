import math

# coords in format: [x0,y0, x1, y1, ....xN, yN]
distance = lambda coords: math.sqrt((coords[2]-coords[0]) ** 2 + (coords[3]-coords[1]) ** 2)

def my_print(label, function, *arguments):
    print(label, function(arguments))

def perimeter(coords):
    xold = coords[0]
    yold = coords[1]
    perimeter = 0
    for i in range(1, len(coords) // 2 ):
        x = coords[2 * i]
        y = coords[2 * i + 1]
        perimeter = perimeter + distance([xold, yold, x, y])
        xold = x
        yold = y
    perimeter = perimeter + distance([xold, yold, coords[0], coords[1]])
    return perimeter

# homework: define area function of coordinates as list - area([x0,y0, x1, y1, ....xN, yN])
# and test it with atleast three different figures

my_print('Distance is: ', distance, 1, 1, 1, 4, 4, 4, 4, 1)
my_print('Perimeter is: ', perimeter, 1, 1, 1, 4, 4, 4, 4, 1)
#my_print('Area is: ', area, 1, 1, 1, 4, 4, 4, 4, 1)
