names = ['Mark', 'Marshall', 'Garry Sobers','Richards', 'Scott Willy']

upperchars = []
for name in names:
    for ch in name:
        if ch.isupper() and ch not in upperchars:
            upperchars.append(ch)

print(upperchars)
            

