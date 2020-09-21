
def mysum(list):
    return 0 if not list else list[0] + mysum(list[1:])

mysum2 = lambda list: 0 if not list else list[0] + mysum(list[1:])

print(mysum([1,2,5,7,9,11]))
print(mysum2([1,2,5,7,9,11]))

