def hello(*users, message = 'Hello'):
    for u in users:
        print(message, u)


hello('Bob', 'Dave', message = 'Hi' )
hello('Li', 'Hu', 'Tim')
