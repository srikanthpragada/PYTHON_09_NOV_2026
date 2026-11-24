def count_upper(st : str) -> int:
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


names = ['Rossum', 'bill', 'Gosling', 'a12', 'denis', 'Andy1']

for cnt in map(count_upper, names):
    print(cnt)