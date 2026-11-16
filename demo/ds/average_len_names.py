# Take names until end is given and display avg length

total_length = 0
count = 0
while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    total_length += len(name)
    count += 1

print('Average Length :', total_length // count)


