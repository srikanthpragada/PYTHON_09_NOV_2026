def iseven(n: int) -> bool:
    """
    Checks whether a number is even
    :param n: Number to check
    :return: True on even false otherwise
    """
    return n % 2 == 0


def isodd(n: int) -> bool:
    return n % 2 != 0


SIZE = 10
INCH_TO_CM = 2.54

if __name__ == '__main__':  # true when you run the module
    print(SIZE)