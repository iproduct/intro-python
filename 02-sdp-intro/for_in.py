for i in range(1, 11, 2):
    print(i)

fruits = ['Ябълка', 'Портокал', 'Круша', 'Череша']
for i in range(len(fruits)):
    print(i + 1, fruits[i], sep=': ', end='\n', file=open('fruits.txt', 'a', encoding='utf-8'), flush=False)

for line in open('fruits.txt', 'r', encoding='utf-8'):
    print(line)