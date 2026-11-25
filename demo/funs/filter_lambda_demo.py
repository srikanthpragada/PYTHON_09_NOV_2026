def has_space(s : str) -> bool:
    return s.find(" ") >= 0

names  = ['Ben king', 'Micheal Jackson', 'Bruce', 'Bolton']

for n in filter(lambda s : s.find(' ') >= 0, names):
    print(n)

for n in filter(has_space, names):
    print(n)