from random import randint

a= []
MAX_VALUE = 20
for i in range(100):
    a.append(randint(0,MAX_VALUE))

def counting_sort(a):
    count = [0 for i in range(MAX_VALUE + 1)]

    for val in a: #counting
        count[val] += 1

    #writing counts to original array
    a.clear()
    for i in range(MAX_VALUE + 1):
        for j in range(count[i]):
            a.append(i)

if __name__ == '__main__':
    print(a)
    counting_sort(a)
    print(a)