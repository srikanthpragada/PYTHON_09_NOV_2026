names = ['Rossum', 'bill', 'Gosling', 'a12', 'denis', 'Andy1']
for name in filter(str.isalpha, names):
    print(name)
