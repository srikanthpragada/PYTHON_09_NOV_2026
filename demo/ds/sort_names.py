# Take names until end is given and display them in sorted order

names = []
while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    names.append(name)

# sort names
names.sort()

for name in names:
    print(name)

