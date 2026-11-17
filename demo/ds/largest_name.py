# Take names until end is given and display the largest name

largest = ""
while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    if name > largest:
        largest = name

print('Largest Name : :', largest)


