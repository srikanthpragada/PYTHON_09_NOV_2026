def count_upper(st : str)-> int:
    count  = 0
    for c in st:
        if c.isupper():
            count += 1

    return count 


c = count_upper('Hello Python')
print(c)