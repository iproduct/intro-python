a= []
for i in range(100):
    a.append(random.randint(1,20))

def counting_sort(a):
    output = []
    count = [0 for i in range(MAX_VALUE)]

    for i in a:
        count[a[i]] += 1

    for i in range(MAX_VALUE):
        for j in range(count[i]):
            output.push(i)

if __name__ == '__main__':
    quick_sort(a)
    print(a)