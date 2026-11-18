# Accept a string which contains names separated by ; and print those names in sorted order
name = input("Enter names [separated by ;]:")
names = name.split(";")
names.sort()
print(names)
