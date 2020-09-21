grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

print(grades.keys())

for key in grades.keys():
    print(key)

l = [k[1] for k in enumerate(grades.keys())]
print(l)