def contains_upper(st: str) -> bool:
    #print(st)
    for c in st:
        if c.isupper():
            return True

    return False

names = ['Rossum', 'bill', 'Gosling', 'denis']
for name in filter(contains_upper, names):
    print(name)