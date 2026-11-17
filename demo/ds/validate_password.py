# Validate password. It must have at least 1 uppercase and 1 digit

pwd = "Abc_123"
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

if not digit:
    print('Invalid Password. Digit is missing!')
    exit()

special = False
for c in pwd:
    if c in "_#@":
        special = True
        break

if special:
    print('Valid Password')
else:
    print('Invalid Password. Special char is missing!')
