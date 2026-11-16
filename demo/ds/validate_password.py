# Validate password. It must have at least 1 uppercase and 1 digit

pwd = "Abc"
# check for uppercase
upper = False
for c in pwd:
    if c.isupper():
        upper = True
        break

if not upper:
    print('Invalid Password. Uppercase is missing!')
    exit()   # terminate the program


digit = False
for c in pwd:
    if c.isdigit():
        digit = True
        break

if digit:
    print('Valid password!')
else:
    print('Invalid Password. Digit is missing!')