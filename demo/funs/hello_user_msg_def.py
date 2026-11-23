def hello(user: str = 'Guest', message: str = 'Hi') -> None:
    print(message, user)


hello('Martin')  # Positional args
hello(message='Hello', user='Henry')  # Keyword args
hello('Scott', 'Hello')
hello()
hello(message='Good Morning')
