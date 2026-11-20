names = ['Andy', 'Anders', 'Bob', 'Cathy']

chars = set()

for n in names:
    chars = chars | set(n)

print(sorted(chars))


