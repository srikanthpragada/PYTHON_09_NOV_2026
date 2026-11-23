def hello(user : str, message : str) -> None:
    print(message, user)


hello('Martin', 'Hi')         # Positional args
hello(message = 'Hi', user = 'Henry')      # Keyword args
hello('Scott', message = 'Hello')     # Mixed

print(10, 20, sep = '*', end = '.')




